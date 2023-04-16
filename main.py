import copy
from vars import *

# The actual funny bit
vgpus = dict()  # vGPU Devices


def parse_device(dev: str, info: dict):
    vgpu = dict()
    vgpu['id'] = info['id']
    vgpu['name'] = info['name']
    vgpu['dev_id'] = {
        'device': dev.split(':')[0],
        'subsystem': dev.split(':')[1]
    }
    vgpu['settings'] = dict()
    if 'ATTR_LIKE' in info.keys():
        if info['ATTR_LIKE'] in device_presets.keys():
            vgpu['settings'] = copy.deepcopy(device_presets[info['ATTR_LIKE']])
        else:
            vgpu_parse = parse_device(info['ATTR_LIKE'], virtual_gpus[info['ATTR_LIKE']])
            vgpu['settings'] = vgpu_parse['settings']
            vgpu['class'] = vgpu_parse['class']
    if 'type' in vgpu['settings'].keys():
        del vgpu['settings']['type']
    if 'FB_LIKE' in info.keys():
        vgpu['settings'].update(framebuffer_sizes[info['FB_LIKE']])
    if 'OVERRIDES' in info.keys():
        for _key, item in info['OVERRIDES'].items():
            vgpu['settings'][_key] = item
    if type(vgpu['settings']['framebuffer']) == str:
        vgpu['settings']['framebuffer'] = int(vgpu['settings']['framebuffer'].lstrip('0x'), 16)
    if type(vgpu['settings']['fbReservation']) == str:
        vgpu['settings']['fbReservation'] = int(vgpu['settings']['fbReservation'].lstrip('0x'), 16)
    if 'profileSize' not in vgpu['settings'].keys():
        vgpu['settings']['profileSize'] = vgpu['settings']['framebuffer'] + vgpu['settings']['fbReservation']
    if 'class' not in vgpu.keys():
        vgpu['class'] = vgpu['settings']['class']
        vgpu['settings'].pop('class')
    if 'license' not in vgpu['settings'].keys():
        vgpu['settings']['license'] = license_types[vgpu['settings']['LICENSE']]
        vgpu['settings'].pop('LICENSE')
    for _key in ['ARCH', 'CONFFILE_PARAMS']:
        if _key in vgpu['settings']:
            vgpu['settings'].pop(_key)
    vgpu['parent'] = {
        'device': dev.split(':')[0],
        'subsystem': '0x0000'
    }
    if 'PGPU_SSID' in info.keys():
        if info['PGPU_SSID'] != 0:
            vgpu['parent']['subsystem'] = info['PGPU_SSID']
    return vgpu


for key in virtual_gpus.keys():
    vgpu_device = parse_device(key, virtual_gpus[key])
    #print(vgpu_device)
    vgpus[vgpu_device['id']] = vgpu_device

myKeys = list(vgpus.keys())
myKeys.sort()
vgpus = {i: vgpus[i] for i in myKeys}

xml = '<?xml version="1.0" encoding="utf-8"?>\n'
xml += '<!DOCTYPE vgpu SYSTEM "http://www.nvidia.com/dtd/vgpuConfig.dtd">\n'
xml += '<vgpuconfig>\n'
xml += '  <version>1.0</version>\n'
xml += '  <globalSettings>\n'
xml += '    <homogeneousVgpus>TRUE</homogeneousVgpus>\n'
xml += '    <pluginSoName>libnvidia-vgpu</pluginSoName>\n'
xml += '  </globalSettings>\n'
for _, device in vgpus.items():
    if device['class'] != 'Geforce':
        continue
    xml += f'  <vgpuType id="{device["id"]}" name="{device["name"]}" class="{device["class"]}">\n'
    xml += f'    <devId vendorId="0x10de" deviceId="{device["dev_id"]["device"]}" subsystemVendorId="0x10de" subsystemId="{device["dev_id"]["subsystem"]}"/>\n'
    xml += f'    <display width="{device["settings"]["display_width"]}" height="{device["settings"]["display_height"]}"/>\n'
    for key, item in device['settings'].items():
        if key in ['profileSize', 'framebuffer', 'fbReservation', 'mappableVideoSize', 'frlConfig', 'encoderCapacity', 'bar1Length'] and type(item) == int:
            xml += f'    <{key}>{hex(item)}</{key}>\n'
        elif key in ['display_width', 'display_height']:
            pass
        else:
            xml += f'    <{key}>{item}</{key}>\n'
    xml += '  </vgpuType>\n'
for pci_id, device in physical_gpus.items():
    device_id = pci_id.split(':')[0]
    subsystem_id = '0x0000'
    if not pci_id.split(':')[1] == str():
        subsystem_id = pci_id.split(':')[1]
    try:
        host_fb_size = framebuffer_sizes[f'{device["GB"]}G']
    except KeyError:
        print('Skipping', device['NAME'], 'as there is no matching VRAM configuration', f'({device["GB"]}G)')
        continue
    host_fb_size = host_fb_size['framebuffer'] + host_fb_size['fbReservation']
    if 'HOSTVGPUMODE' in device.keys():
        xml += f'  <pgpu fractionalMultiVgpu="{device["fractionalMultiVgpu"]}" hostVgpuMode="{device["HOSTVGPUMODE"].lower()}">\n'
    else:
        xml += f'  <pgpu fractionalMultiVgpu="{device["fractionalMultiVgpu"]}">\n'
    xml += f'    <devId vendorId="0x10de" deviceId="{device_id}" subsystemVendorId="0x10de" subsystemId="{subsystem_id}"/>\n'
    for _, vgpu_device in vgpus.items():
        if vgpu_device['parent']['device'] == device_id and vgpu_device['parent']['subsystem'] == subsystem_id:
            xml += f'    <supportedVgpu vgpuId="{vgpu_device["id"]}">\n'
            xml += f'      <maxVgpus>{int(host_fb_size / vgpu_device["settings"]["profileSize"])}</maxVgpus>\n'
            xml += '       <digest type="signature">38fc196fcdd9f48ada0737791291d1fa93ae96fd0f517cef43b715bbbb50c37231308f3fecff1faf2fa0c16a0136e1813b15ab1c66b53d9cd370686d525f0c803bca564f21a7efe0c05147f02a3f59e35004a1627afd5f8bc433ab07d71006ace26c75cf3a32e5cc3e1859057b0c01bdb3e87003b2e8b9474c0733cb6d6ff9e4</digest>\n'
            xml += '    </supportedVgpu>\n'
    xml += '  </pgpu>\n'
xml += '</vgpuconfig>\n'

fh = open('vgpuConfig.xml', 'w')
fh.write(xml)
fh.close()