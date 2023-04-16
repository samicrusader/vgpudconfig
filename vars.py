license_types = {
    'VWS': 'QVDWS;VWS;VWSExt',
    'VAPPS': 'VApps',
    'VPC': 'VPC;QVDWS;VWS;VWSExt',
    'COMPUTE': 'VCS;QVDWS',
    'GAMING': 'VGaming'
}

framebuffer_sizes = {
    'HALFG': {
        'framebuffer': 0x1A000000,
        'fbReservation': 0x6000000
    },
    '1G': {
        'framebuffer': 0x38000000,
        'fbReservation': 0x8000000
    },
    '2G': {
        'framebuffer': 0x74000000,
        'fbReservation': 0xC000000
    },
    '3G': {
        'framebuffer': 0xB0000000,
        'fbReservation': 0x10000000
    },
    '4G': {
        'framebuffer': 0xEC000000,
        'fbReservation': 0x14000000
    },
    '5G': {
        'framebuffer': 0x128000000,
        'fbReservation': 0x18000000
    },
    '6G': {
        'framebuffer': 0x164000000,
        'fbReservation': 0x1C000000
    },
    '8G': {
        'framebuffer': 0x1DC000000,
        'fbReservation': 0x24000000
    },
    '10G': {
        'framebuffer': 0x254000000,
        'fbReservation': 0x2C000000
    },
    '12G': {
        'framebuffer': 0x2CC000000,
        'fbReservation': 0x34000000
    },
    '16G': {
        'framebuffer': 0x3BC000000,
        'fbReservation': 0x44000000
    },
    '20G': {
        'framebuffer': 0x4AC000000,
        'fbReservation': 0x54000000
    },
    '24G': {
        'framebuffer': 0x59C000000,
        'fbReservation': 0x64000000
    },
    '32G': {
        'framebuffer': 0x77C000000,
        'fbReservation': 0x84000000
    },
    '40G': { # From the original vgpuConfig.xml
        'framebuffer': 0x95C000000,
        'fbReservation': 0xA4000000
    },
    '48G': {
        'framebuffer': 0xB3C000000,
        'fbReservation': 0xC4000000
    },
    '80G': {
        'framebuffer': 0x12BC000000,
        'fbReservation': 0x144000000
    }
}

device_presets = {
    'VAPPS_ATTRIBUTES': {
        'class': 'NVS',
        'numHeads': 1,
        'display_width': 1280,
        'display_height': 1024,
        'maxPixels': 1310720,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 0,
        'eccSupported': 0,
        'multiVgpuSupported': 0,
        'LICENSE': 'VAPPS',
        'type': 'is_nvs',
    },
    'VPC_ATTRIBUTES': {
        'class': 'NVS',
        'numHeads': 4,
        'display_width': 5120,
        'display_height': 2880,
        'maxPixels': 16384000,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x2d,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 0,
        'eccSupported': 0,
        'multiVgpuSupported': 0,
        'LICENSE': 'VPC',
        'type': 'is_nvs',
    },
    'QVDWS_ATTRIBUTES': {
        'class': 'Quadro',
        'numHeads': 4,
        'display_width': 7680,
        'display_height': 4320,
        'maxPixels': 66355200,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 1,
        'eccSupported': 1,
        'multiVgpuSupported': 0,
        'LICENSE': 'VWS',
        'type': 'is_grid',
    },
    'COMPUTE_ATTRIBUTES': {
        'class': 'Compute',
        'numHeads': 1,
        'display_width': 4096,
        'display_height': 2160,
        'maxPixels': 8847360,
        'bar1Length': 0x1000,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 1,
        'eccSupported': 1,
        'multiVgpuSupported': 0,
        'LICENSE': 'COMPUTE',
        'type': 'is_vcompute',
    },
    'NGN_ATTRIBUTES': {
        'class': 'Geforce',
        'numHeads': 1,
        'display_width': 4096,
        'display_height': 2160,
        'maxPixels': 8847360,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 1,
        'eccSupported': 0,
        'multiVgpuSupported': 0,
        'LICENSE': 'GAMING',
        'CONFFILE_PARAMS': {
            'ALL': {
                'vgpu_device_caps': 0,
                'pte_blit_enabled': 0,
                'cilp_disabled_on_wddm': 1,
            },
        },
        'type': 'is_ngn',
    },
    'GAMING_ATTRIBUTES': {
        'class': 'Geforce',
        'numHeads': 1,
        'display_width': 4096,
        'display_height': 2160,
        'maxPixels': 8847360,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 1,
        'eccSupported': 0,
        'multiVgpuSupported': 0,
        'LICENSE': 'GAMING',
        'type': 'is_vgaming',
    },
    'GAMING_NGN_ATTRIBUTES': {
        'class': 'Geforce',
        'numHeads': 1,
        'display_width': 4096,
        'display_height': 2160,
        'maxPixels': 8847360,
        'bar1Length': 0x100,
        'encoderCapacity': 0x64,
        'frame_rate_limiter': 1,
        'frlConfig': 0x3c,
        'mappableVideoSize': 0x400000,
        'cudaEnabled': 1,
        'eccSupported': 0,
        'multiVgpuSupported': 0,
        'LICENSE': 'GAMING',
        'ARCH': 'amd64',
        'CONFFILE_PARAMS': {
            'is_ngn': {
                'cilp_disabled_on_wddm': 1,
            },
        },
        'type': 'is_vgaming_ngn',
    }
}

physical_gpus = {
    '0x13F2:': {
        'NAME': 'Tesla M60',
        'DEVICECLASS': 'GM204GL',
        'GB': 8,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x13F3:': {
        'NAME': 'Tesla M6',
        'DEVICECLASS': 'GM204GL',
        'GB': 8,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x13BD:0x1160': {
        'NAME': 'Tesla M10',
        'SSNAME': 'Tesla M10',
        'DEVICECLASS': 'GM107GL',
        'GB': 8,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1B38:': {
        'NAME': 'Tesla P40',
        'DEVICECLASS': 'GP102GL',
        'GB': 24,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1BB3:': {
        'NAME': 'Tesla P4',
        'DEVICECLASS': 'GP104GL',
        'GB': 8,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1BB4:': {
        'NAME': 'Tesla P6',
        'DEVICECLASS': 'GP104GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x15F8:': {
        'NAME': 'Tesla P100-PCIE-16GB',
        'DEVICECLASS': 'GP100GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x15F9:': {
        'NAME': 'Tesla P100-SXM2-16GB',
        'DEVICECLASS': 'GP100GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1DB4:': {
        'NAME': 'Tesla V100-PCIE-16GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1DB1:': {
        'NAME': 'Tesla V100-SXM2-16GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x15F7:': {
        'NAME': 'Tesla P100-PCIE-12GB',
        'DEVICECLASS': 'GP100GL',
        'GB': 12,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1DB3:': {
        'NAME': 'Tesla V100-FHHL-16GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1DB6:': {
        'NAME': 'Tesla V100-PCIE-32GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 32,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1DB5:': {
        'NAME': 'Tesla V100-SXM2-32GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 32,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1EB8:': {
        'NAME': 'Tesla T4',
        'DEVICECLASS': 'TU104GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1E37:0x1304': {
        'NAME': 'PG150 SKU215/SKU220',
        'SSNAME': 'PG150 SKU220',
        'DEVICECLASS': 'TU102GL',
        'GB': 8,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1E37:0x1370': {
        'NAME': 'PG150 SKU215/SKU220',
        'SSNAME': 'PG150 SKU215',
        'DEVICECLASS': 'TU102GL',
        'GB': 16,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 0
    },
    '0x1E30:0x12BA': {
        'NAME': 'Quadro RTX 6000/8000',
        'SSNAME': 'Quadro RTX 6000',
        'DEVICECLASS': 'TU102GL',
        'GB': 24,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x1E30:0x129E': {
        'NAME': 'Quadro RTX 6000/8000',
        'SSNAME': 'Quadro RTX 8000',
        'DEVICECLASS': 'TU102GL',
        'GB': 48,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x1DF6:0x13D6': {
        'NAME': 'Tesla V100S-PCIE-32GB',
        'SSNAME': 'Tesla V100S-PCIE-32GB',
        'DEVICECLASS': 'GV100GL',
        'GB': 32,
        'DISABLE_ON': ['hyperv'],
        'fractionalMultiVgpu': 1
    },
    '0x1E78:0x13D9': {
        'NAME': 'Quadro RTX 6000/8000',
        'SSNAME': 'Quadro RTX 6000',
        'DEVICECLASS': 'TU102GL',
        'GB': 24,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x1E78:0x13D8': {
        'NAME': 'Quadro RTX 6000/8000',
        'SSNAME': 'Quadro RTX 8000',
        'DEVICECLASS': 'TU102GL',
        'GB': 48,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x20B0:': {
        'NAME': 'NVIDIA A100-SXM4-40GB',
        'DEVICECLASS': 'GA100',
        'GB': 40,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x20F1:': {
        'NAME': 'NVIDIA A100-PCIE-40GB',
        'DEVICECLASS': 'GA100',
        'GB': 40,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x20BE:': {
        'NAME': 'NVIDIA A100',
        'DEVICECLASS': 'GA100',
        'GB': 40,
        'HOSTVGPUMODE': 'SRIOV',
        'INTERNAL': 1,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x20BF:': {
        'NAME': 'NVIDIA A100',
        'DEVICECLASS': 'GA100',
        'GB': 40,
        'HOSTVGPUMODE': 'SRIOV',
        'INTERNAL': 1,
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x2230:': {
        'NAME': 'NVIDIA RTX A6000',
        'DEVICECLASS': 'GA102',
        'GB': 48,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x2235:': {
        'NAME': 'NVIDIA A40',
        'DEVICECLASS': 'GA102',
        'GB': 48,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x2236:': {
        'NAME': 'NVIDIA A10',
        'DEVICECLASS': 'GA102',
        'GB': 24,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x20B2:': {
        'NAME': 'NVIDIA A100-SXM4-80GB',
        'DEVICECLASS': 'GA102',
        'GB': 80,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x2237:': {
        'NAME': 'NVIDIA A10G',
        'DEVICECLASS': 'GA102',
        'GB': 24,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'kvm', 'xenserver', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
    '0x2231:': {
        'NAME': 'NVIDIA RTX A5000',
        'DEVICECLASS': 'GA102',
        'GB': 24,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x2233:0x165A': {
        'NAME': 'NVIDIA RTX A5500',
        'SSNAME': 'NVIDIA RTX A5500',
        'DEVICECLASS': 'GA102',
        'GB': 24,
        'HOSTVGPUMODE': 'SRIOV',
        'fractionalMultiVgpu': 1
    },
    '0x20B5:0x1533': {
        'NAME': 'NVIDIA A100-PCIE-80GB',
        'SSNAME': 'NVIDIA A100-PCIE-80GB',
        'DEVICECLASS': 'GA100',
        'GB': 80,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'ALIASES': {
            '0x20B8:0x1581': 'NVIDIA A100X'
        },
        'fractionalMultiVgpu': 1
    },
    '0x20B7:0x1532': {
        'NAME': 'NVIDIA A30',
        'SSNAME': 'NVIDIA A30',
        'DEVICECLASS': 'GA100',
        'GB': 24,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'ALIASES': {
            '0x20B9:0x157F': 'NVIDIA A30X'
        },
        'fractionalMultiVgpu': 1
    },
    '0x25B6:0x14A9': {
        'NAME': 'NVIDIA A16/NVIDIA A2',
        'SSNAME': 'NVIDIA A16',
        'DEVICECLASS': 'GA107',
        'GB': 16,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x25B6:0x157E': {
        'NAME': 'NVIDIA A16/NVIDIA A2',
        'SSNAME': 'NVIDIA A2',
        'DEVICECLASS': 'GA107',
        'GB': 16,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7'],
        'fractionalMultiVgpu': 1
    },
    '0x2238:0x1677': {
        'NAME': 'NVIDIA A10M',
        'SSNAME': 'NVIDIA A10M',
        'DEVICECLASS': 'GA102',
        'GB': 20,
        'HOSTVGPUMODE': 'SRIOV',
        'DISABLE_ON': ['hyperv', 'esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0'],
        'fractionalMultiVgpu': 1
    },
}

virtual_gpus = {
    #
    # 0.5 GB Profiles
    #
    '0x13F2:0x1176': {
        'id': 11,
        'name': 'GRID M60-0B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
        },
    },
    '0x13F2:0x114C': {
        'id': 12,
        'name': 'GRID M60-0Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
            'cudaEnabled': 0,
        },
    },
    '0x13F3:0x117E': {
        'id': 23,
        'name': 'GRID M6-0B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
        },
    },
    '0x13F3:0x1180': {
        'id': 24,
        'name': 'GRID M6-0Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
            'cudaEnabled': 0,
        },
    },
    '0x13BD:0x11CC': {
        'id': 35,
        'name': 'GRID M10-0B',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
        },
    },
    '0x13BD:0x11CE': {
        'id': 36,
        'name': 'GRID M10-0Q',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'OVERRIDES': {
            'eccSupported': 0,
            'numHeads': 2,
            'display_width': 2560,
            'display_height': 1600,
            'maxPixels': 8192000,
            'cudaEnabled': 0,
        },
    },
    #
    # 1 GB Profiles
    #
    '0x13F2:0x11AE': {
        'id': 13,
        'name': 'GRID M60-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x13F2:0x1177': {
        'id': 14,
        'name': 'GRID M60-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
        },
    },
    '0x13F2:0x1337': {
        'id': 238,
        'name': 'GRID M60-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x1177',  # M60-1B
    },
    '0x13F2:0x114D': {
        'id': 15,
        'name': 'GRID M60-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 17694720,
            'cudaEnabled': 0,
        },
    },
    '0x13F3:0x11AA': {
        'id': 25,
        'name': 'GRID M6-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x13F3:0x117F': {
        'id': 26,
        'name': 'GRID M6-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
        },
    },
    '0x13F3:0x1338': {
        'id': 239,
        'name': 'GRID M6-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F3:0x117F',  # M6-1B
    },
    '0x13F3:0x1181': {
        'id': 27,
        'name': 'GRID M6-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 17694720,
            'cudaEnabled': 0,
        },
    },
    '0x13BD:0x11D3': {
        'id': 37,
        'name': 'GRID M10-1A',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x13BD:0x11CD': {
        'id': 38,
        'name': 'GRID M10-1B',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
        },
    },
    '0x13BD:0x1339': {
        'id': 240,
        'name': 'GRID M10-1B4',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13BD:0x11CD',  # M10-1B
    },
    '0x13BD:0x11CF': {
        'id': 39,
        'name': 'GRID M10-1Q',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 17694720,
            'eccSupported': 0,
            'cudaEnabled': 0,
        },
    },
    '0x1B38:0x11E8': {
        'id': 46,
        'name': 'GRID P40-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 17694720,
        },
    },
    '0x1B38:0x11F0': {
        'id': 54,
        'name': 'GRID P40-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x1B38:0x11E7': {
        'id': 62,
        'name': 'GRID P40-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '1G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 16384000,
        },
    },
    '0x1B38:0x133A': {
        'id': 241,
        'name': 'GRID P40-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1BB3:0x1204': {
        'id': 63,
        'name': 'GRID P4-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1BB3:0x1208': {
        'id': 67,
        'name': 'GRID P4-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x1BB3:0x1203': {
        'id': 71,
        'name': 'GRID P4-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1BB3:0x133C': {
        'id': 243,
        'name': 'GRID P4-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1BB4:0x11F9': {
        'id': 72,
        'name': 'GRID P6-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1BB4:0x11FE': {
        'id': 77,
        'name': 'GRID P6-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '1G',
    },
    '0x1BB4:0x11F8': {
        'id': 82,
        'name': 'GRID P6-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1BB4:0x133B': {
        'id': 242,
        'name': 'GRID P6-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F8:0x1222': {
        'id': 83,
        'name': 'GRID P100-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x15F8:0x1227': {
        'id': 88,
        'name': 'GRID P100-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x15F8:0x1221': {
        'id': 93,
        'name': 'GRID P100-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F8:0x133D': {
        'id': 244,
        'name': 'GRID P100-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F9:0x122D': {
        'id': 94,
        'name': 'GRID P100X-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x15F9:0x1232': {
        'id': 99,
        'name': 'GRID P100X-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x15F9:0x122C': {
        'id': 104,
        'name': 'GRID P100X-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F9:0x133E': {
        'id': 245,
        'name': 'GRID P100X-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB4:0x124F': {
        'id': 105,
        'name': 'GRID V100-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DB4:0x1254': {
        'id': 110,
        'name': 'GRID V100-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DB4:0x124E': {
        'id': 115,
        'name': 'GRID V100-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB4:0x1340': {
        'id': 247,
        'name': 'GRID V100-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB1:0x125A': {
        'id': 116,
        'name': 'GRID V100X-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DB1:0x125F': {
        'id': 121,
        'name': 'GRID V100X-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DB1:0x1259': {
        'id': 126,
        'name': 'GRID V100X-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB1:0x1341': {
        'id': 248,
        'name': 'GRID V100X-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F7:0x1266': {
        'id': 144,
        'name': 'GRID P100C-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x15F7:0x126B': {
        'id': 149,
        'name': 'GRID P100C-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x15F7:0x1265': {
        'id': 154,
        'name': 'GRID P100C-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x15F7:0x133F': {
        'id': 246,
        'name': 'GRID P100C-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB3:0x1292': {
        'id': 165,
        'name': 'GRID V100L-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DB3:0x1297': {
        'id': 170,
        'name': 'GRID V100L-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DB3:0x1290': {
        'id': 175,
        'name': 'GRID V100L-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB3:0x1344': {
        'id': 251,
        'name': 'GRID V100L-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB6:0x12BF': {
        'id': 180,
        'name': 'GRID V100D-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DB6:0x12C5': {
        'id': 186,
        'name': 'GRID V100D-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DB6:0x12BD': {
        'id': 192,
        'name': 'GRID V100D-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB6:0x1342': {
        'id': 249,
        'name': 'GRID V100D-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB5:0x12CD': {
        'id': 194,
        'name': 'GRID V100DX-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DB5:0x12D3': {
        'id': 200,
        'name': 'GRID V100DX-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DB5:0x12CB': {
        'id': 206,
        'name': 'GRID V100DX-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1DB5:0x1343': {
        'id': 250,
        'name': 'GRID V100DX-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1EB8:0x130C': {
        'id': 230,
        'name': 'GRID T4-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1EB8:0x1311': {
        'id': 225,
        'name': 'GRID T4-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1EB8:0x1309': {
        'id': 222,
        'name': 'GRID T4-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1EB8:0x1345': {
        'id': 252,
        'name': 'GRID T4-1B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1E30:0x1325': {
        'id': 256,
        'name': 'GRID RTX6000-1Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1E30:0x132D': {
        'id': 264,
        'name': 'GRID RTX8000-1Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'max_instance': 32,
        },
    },
    '0x1DF6:0x13E5': {
        'id': 355,
        'name': 'GRID V100S-1Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1DF6:0x13EB': {
        'id': 365,
        'name': 'GRID V100S-1A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1DF6:0x13E1': {
        'id': 371,
        'name': 'GRID V100S-1B',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1E78:0x13F9': {
        'id': 375,
        'name': 'GRID RTX6000P-1Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x1E78:0x13F7': {
        'id': 400,
        'name': 'GRID RTX6000P-1B',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1E30:0x1437': {
        'id': 435,
        'name': 'GRID RTX6000-1B',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1E78:0x1401': {
        'id': 392,
        'name': 'GRID RTX6000P-1A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1E30:0x1439': {
        'id': 437,
        'name': 'GRID RTX6000-1A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x1E78:0x1414': {
        'id': 404,
        'name': 'GRID RTX8000P-1Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x132D',  # RTX8000-1Q
    },
    '0x1E78:0x141E': {
        'id': 414,
        'name': 'GRID RTX8000P-1A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'max_instance': 32,
        },
    },
    '0x1E30:0x1443': {
        'id': 447,
        'name': 'GRID RTX8000-1A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'max_instance': 32,
        },
    },
    '0x1E78:0x1412': {
        'id': 402,
        'name': 'GRID RTX8000P-1B',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x1E30:0x1441': {
        'id': 445,
        'name': 'GRID RTX8000-1B',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    #
    # 2 GB Profiles
    #
    '0x13F2:0x11AF': {
        'id': 16,
        'name': 'GRID M60-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '2G',
    },
    '0x13F2:0x117D': {
        'id': 17,
        'name': 'GRID M60-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '2G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 17694720,
        },
    },
    '0x13F2:0x12EC': {
        'id': 210,
        'name': 'GRID M60-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x13F2:0x114E': {
        'id': 18,
        'name': 'GRID M60-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '2G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 35389440,
            'cudaEnabled': 0,
        },
    },
    '0x13F3:0x11AB': {
        'id': 28,
        'name': 'GRID M6-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
    },
    '0x13F3:0x117C': {
        'id': 29,
        'name': 'GRID M6-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x13F3:0x12ED': {
        'id': 209,
        'name': 'GRID M6-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x13F3:0x1182': {
        'id': 30,
        'name': 'GRID M6-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x114E',  # M60-2Q
    },
    '0x13BD:0x11D4': {
        'id': 40,
        'name': 'GRID M10-2A',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
    },
    '0x13BD:0x1286': {
        'id': 155,
        'name': 'GRID M10-2B',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x13BD:0x12EE': {
        'id': 208,
        'name': 'GRID M10-2B4',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x13BD:0x11D0': {
        'id': 41,
        'name': 'GRID M10-2Q',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x114E',  # M60-2Q
        'OVERRIDES': {
            'eccSupported': 0,
        },
    },
    '0x1B38:0x11E9': {
        'id': 47,
        'name': 'GRID P40-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '2G',
        'OVERRIDES': {
            'maxPixels': 35389440,
        },
    },
    '0x1B38:0x11F1': {
        'id': 55,
        'name': 'GRID P40-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '2G',
    },
    '0x1B38:0x1287': {
        'id': 156,
        'name': 'GRID P40-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VPC_ATTRIBUTES',
        'FB_LIKE': '2G',
        'OVERRIDES': {
            'maxPixels': 17694720,
        },
    },
    '0x1B38:0x12EF': {
        'id': 215,
        'name': 'GRID P40-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1BB3:0x1205': {
        'id': 64,
        'name': 'GRID P4-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1BB3:0x1209': {
        'id': 68,
        'name': 'GRID P4-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1BB3:0x1288': {
        'id': 157,
        'name': 'GRID P4-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1BB3:0x12F1': {
        'id': 214,
        'name': 'GRID P4-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1BB3:0x136D': {
        'id': 274,
        'name': 'GRID GTX P4-2',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '2G',
        'ARCH': 'amd64',
    },
    '0x1BB4:0x11FA': {
        'id': 73,
        'name': 'GRID P6-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1BB4:0x11FF': {
        'id': 78,
        'name': 'GRID P6-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1BB4:0x1289': {
        'id': 158,
        'name': 'GRID P6-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1BB4:0x12F0': {
        'id': 216,
        'name': 'GRID P6-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F8:0x1223': {
        'id': 84,
        'name': 'GRID P100-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x15F8:0x1228': {
        'id': 89,
        'name': 'GRID P100-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x15F8:0x128C': {
        'id': 160,
        'name': 'GRID P100-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F8:0x12F2': {
        'id': 211,
        'name': 'GRID P100-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F9:0x122E': {
        'id': 95,
        'name': 'GRID P100X-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x15F9:0x1233': {
        'id': 100,
        'name': 'GRID P100X-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x15F9:0x128B': {
        'id': 159,
        'name': 'GRID P100X-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F9:0x12F3': {
        'id': 213,
        'name': 'GRID P100X-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB4:0x1250': {
        'id': 106,
        'name': 'GRID V100-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DB4:0x1255': {
        'id': 111,
        'name': 'GRID V100-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DB4:0x128F': {
        'id': 163,
        'name': 'GRID V100-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB4:0x12F5': {
        'id': 217,
        'name': 'GRID V100-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB1:0x125B': {
        'id': 117,
        'name': 'GRID V100X-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DB1:0x1260': {
        'id': 122,
        'name': 'GRID V100X-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DB1:0x128E': {
        'id': 162,
        'name': 'GRID V100X-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB1:0x12F6': {
        'id': 221,
        'name': 'GRID V100X-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F7:0x1267': {
        'id': 145,
        'name': 'GRID P100C-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x15F7:0x126C': {
        'id': 150,
        'name': 'GRID P100C-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x15F7:0x128D': {
        'id': 161,
        'name': 'GRID P100C-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x15F7:0x12F4': {
        'id': 212,
        'name': 'GRID P100C-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB3:0x1293': {
        'id': 166,
        'name': 'GRID V100L-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DB3:0x1298': {
        'id': 171,
        'name': 'GRID V100L-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DB3:0x1291': {
        'id': 176,
        'name': 'GRID V100L-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB3:0x12F9': {
        'id': 220,
        'name': 'GRID V100L-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB6:0x12C0': {
        'id': 181,
        'name': 'GRID V100D-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DB6:0x12C6': {
        'id': 187,
        'name': 'GRID V100D-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DB6:0x12BE': {
        'id': 193,
        'name': 'GRID V100D-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB6:0x12F7': {
        'id': 218,
        'name': 'GRID V100D-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB5:0x12CE': {
        'id': 195,
        'name': 'GRID V100DX-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DB5:0x12D4': {
        'id': 201,
        'name': 'GRID V100DX-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DB5:0x12CC': {
        'id': 207,
        'name': 'GRID V100DX-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1DB5:0x12F8': {
        'id': 219,
        'name': 'GRID V100DX-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1EB8:0x130D': {
        'id': 231,
        'name': 'GRID T4-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1EB8:0x1312': {
        'id': 226,
        'name': 'GRID T4-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1EB8:0x130A': {
        'id': 223,
        'name': 'GRID T4-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1EB8:0x130B': {
        'id': 224,
        'name': 'GRID T4-2B4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1E37:0x13A7': {
        'id': 322,
        'name': 'GRID RTX T10x-2',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '2G',
        'ARCH': 'amd64',
    },
    '0x1E37:0x1349': {
        'id': 237,
        'name': 'GeForce RTX T10x-2',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '2G',
    },
    '0x1E30:0x1326': {
        'id': 257,
        'name': 'GRID RTX6000-2Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1E30:0x132E': {
        'id': 265,
        'name': 'GRID RTX8000-2Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DF6:0x13E6': {
        'id': 356,
        'name': 'GRID V100S-2Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1DF6:0x13EC': {
        'id': 366,
        'name': 'GRID V100S-2A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1DF6:0x13E3': {
        'id': 373,
        'name': 'GRID V100S-2B',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1E78:0x13FA': {
        'id': 376,
        'name': 'GRID RTX6000P-2Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1E78:0x13F8': {
        'id': 401,
        'name': 'GRID RTX6000P-2B',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1E30:0x1438': {
        'id': 436,
        'name': 'GRID RTX6000-2B',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1E78:0x1402': {
        'id': 393,
        'name': 'GRID RTX6000P-2A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1E30:0x143A': {
        'id': 438,
        'name': 'GRID RTX6000-2A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1E78:0x1415': {
        'id': 405,
        'name': 'GRID RTX8000P-2Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x1E78:0x141F': {
        'id': 415,
        'name': 'GRID RTX8000P-2A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1E30:0x1444': {
        'id': 448,
        'name': 'GRID RTX8000-2A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F1',  # P40-2A
    },
    '0x1E78:0x1413': {
        'id': 403,
        'name': 'GRID RTX8000P-2B',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    '0x1E30:0x1442': {
        'id': 446,
        'name': 'GRID RTX8000-2B',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x1287',  # P40-2B
    },
    #
    # 3 GB Profiles
    #
    '0x1B38:0x11EA': {
        'id': 48,
        'name': 'GRID P40-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '3G',
        'OVERRIDES': {
            'maxPixels': 35389440,
        },
    },
    '0x1B38:0x11F2': {
        'id': 56,
        'name': 'GRID P40-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '3G',
    },
    '0x1E30:0x1327': {
        'id': 258,
        'name': 'GRID RTX6000-3Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
    },
    '0x1E30:0x132F': {
        'id': 266,
        'name': 'GRID RTX8000-3Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
    },
    '0x1E78:0x13FB': {
        'id': 377,
        'name': 'GRID RTX6000P-3Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
    },
    '0x1E78:0x1403': {
        'id': 394,
        'name': 'GRID RTX6000P-3A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
    },
    '0x1E30:0x143B': {
        'id': 439,
        'name': 'GRID RTX6000-3A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
    },
    '0x1E78:0x1416': {
        'id': 406,
        'name': 'GRID RTX8000P-3Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
    },
    '0x1E78:0x1420': {
        'id': 416,
        'name': 'GRID RTX8000P-3A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
    },
    '0x1E30:0x1445': {
        'id': 449,
        'name': 'GRID RTX8000-3A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
    },
    #
    # 4 GB Profiles
    #
    '0x13F2:0x11B0': {
        'id': 19,
        'name': 'GRID M60-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x13F2:0x114F': {
        'id': 20,
        'name': 'GRID M60-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '4G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 35389440,
            'cudaEnabled': 0,
        },
    },
    '0x13F3:0x11AC': {
        'id': 31,
        'name': 'GRID M6-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
    },
    '0x13F3:0x1183': {
        'id': 32,
        'name': 'GRID M6-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x114F',  # M60-4Q
    },
    '0x13BD:0x11D5': {
        'id': 42,
        'name': 'GRID M10-4A',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
    },
    '0x13BD:0x11D1': {
        'id': 43,
        'name': 'GRID M10-4Q',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x114F',  # M60-4Q
        'OVERRIDES': {
            'eccSupported': 0,
        },
    },
    '0x1B38:0x11EB': {
        'id': 49,
        'name': 'GRID P40-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x114F',  # M60-4Q
        'OVERRIDES': {
            'display_width': 7680,
            'display_height': 4320,
            'maxPixels': 58982400,
            'cudaEnabled': 1,
        },
    },
    '0x1B38:0x1381': {
        'id': 283,
        'name': 'GRID P40-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1B38:0x11F3': {
        'id': 57,
        'name': 'GRID P40-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1BB3:0x1206': {
        'id': 65,
        'name': 'GRID P4-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1BB3:0x1385': {
        'id': 288,
        'name': 'GRID P4-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x1BB3:0x120A': {
        'id': 69,
        'name': 'GRID P4-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1BB3:0x136E': {
        'id': 275,
        'name': 'GRID GTX P4-4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '4G',
        'ARCH': 'amd64',
    },
    '0x1BB4:0x11FB': {
        'id': 74,
        'name': 'GRID P6-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1BB4:0x1386': {
        'id': 290,
        'name': 'GRID P6-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1BB4:0x1200': {
        'id': 79,
        'name': 'GRID P6-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x15F8:0x1224': {
        'id': 85,
        'name': 'GRID P100-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x15F8:0x138A': {
        'id': 293,
        'name': 'GRID P100-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C

    },
    '0x15F8:0x1229': {
        'id': 90,
        'name': 'GRID P100-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x15F9:0x122F': {
        'id': 96,
        'name': 'GRID P100X-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x15F9:0x1388': {
        'id': 296,
        'name': 'GRID P100X-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x15F9:0x1234': {
        'id': 101,
        'name': 'GRID P100X-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1DB4:0x1251': {
        'id': 107,
        'name': 'GRID V100-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DB4:0x1393': {
        'id': 299,
        'name': 'GRID V100-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DB4:0x1256': {
        'id': 112,
        'name': 'GRID V100-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1DB1:0x125C': {
        'id': 118,
        'name': 'GRID V100X-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DB1:0x138E': {
        'id': 302,
        'name': 'GRID V100X-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DB1:0x1261': {
        'id': 123,
        'name': 'GRID V100X-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x15F7:0x1268': {
        'id': 146,
        'name': 'GRID P100C-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x15F7:0x138C': {
        'id': 305,
        'name': 'GRID P100C-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x15F7:0x126D': {
        'id': 151,
        'name': 'GRID P100C-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1DB3:0x1294': {
        'id': 167,
        'name': 'GRID V100L-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DB3:0x1398': {
        'id': 308,
        'name': 'GRID V100L-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DB3:0x1299': {
        'id': 172,
        'name': 'GRID V100L-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1DB6:0x12C1': {
        'id': 182,
        'name': 'GRID V100D-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DB6:0x1395': {
        'id': 311,
        'name': 'GRID V100D-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DB6:0x12C7': {
        'id': 188,
        'name': 'GRID V100D-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1DB5:0x12CF': {
        'id': 196,
        'name': 'GRID V100DX-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DB5:0x1390': {
        'id': 315,
        'name': 'GRID V100DX-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DB5:0x12D5': {
        'id': 202,
        'name': 'GRID V100DX-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1EB8:0x130E': {
        'id': 232,
        'name': 'GRID T4-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1EB8:0x139A': {
        'id': 319,
        'name': 'GRID T4-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x20B0:0x1474': {
        'id': 457,
        'name': 'GRID A100X-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1475': {
        'id': 458,
        'name': 'GRID A100X-5C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
            'framebuffer': '0x128000000',
            'fbReservation': '0x18000000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1476': {
        'id': 459,
        'name': 'GRID A100X-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
            'framebuffer': '0x1DC000000',
            'fbReservation': '0x24000000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1477': {
        'id': 460,
        'name': 'GRID A100X-10C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
            'framebuffer': '0x254000000',
            'fbReservation': '0x2C000000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1478': {
        'id': 461,
        'name': 'GRID A100X-20C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
            'framebuffer': '0x4AC000000',
            'fbReservation': '0x54000000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1479': {
        'id': 462,
        'name': 'GRID A100X-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x400',
            'framebuffer': '0x95C000000',
            'fbReservation': '0xA4000000',
            'multiVgpuSupported': 1,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x146F': {
        'id': 463,
        'name': 'GRID A100X-1-5C',
        'ATTR_LIKE': '0x20B0:0x1475',
        'OVERRIDES': {
            'gpuInstanceSize': 1,
            'max_instance': 7,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x160C': {
        'id': 704,
        'name': 'GRID A100X-1-5CME',
        'ATTR_LIKE': '0x20B0:0x146F',
        'DISABLE_ON': ['esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0', ],
        'OVERRIDES': {
            'max_instance': 1,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1470': {
        'id': 464,
        'name': 'GRID A100X-2-10C',
        'ATTR_LIKE': '0x20B0:0x1477',
        'OVERRIDES': {
            'gpuInstanceSize': 2,
            'max_instance': 3,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1471': {
        'id': 465,
        'name': 'GRID A100X-3-20C',
        'ATTR_LIKE': '0x20B0:0x1478',
        'OVERRIDES': {
            'gpuInstanceSize': 3,
            'max_instance': 2,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1472': {
        'id': 466,
        'name': 'GRID A100X-4-20C',
        'ATTR_LIKE': '0x20B0:0x1478',
        'OVERRIDES': {
            'gpuInstanceSize': 4,
            'max_instance': 1,
        },
        'gpuDirectSupported': 1,
    },
    '0x20B0:0x1473': {
        'id': 467,
        'name': 'GRID A100X-7-40C',
        'ATTR_LIKE': '0x20B0:0x1479',
        'OVERRIDES': {
            'gpuInstanceSize': 7,
            'max_instance': 1,
            'multiVgpuSupported': 0,
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1498': {
        'id': 468,
        'name': 'GRID A100-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1474',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1499': {
        'id': 469,
        'name': 'GRID A100-5C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1475',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x149A': {
        'id': 470,
        'name': 'GRID A100-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1476',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x149B': {
        'id': 471,
        'name': 'GRID A100-10C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1477',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x149C': {
        'id': 472,
        'name': 'GRID A100-20C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1478',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x149D': {
        'id': 473,
        'name': 'GRID A100-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1479',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1493': {
        'id': 474,
        'name': 'GRID A100-1-5C',
        'ATTR_LIKE': '0x20B0:0x146F',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x160E': {
        'id': 706,
        'name': 'GRID A100-1-5CME',
        'ATTR_LIKE': '0x20F1:0x1493',
        'DISABLE_ON': ['esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0', ],
        'OVERRIDES': {
            'max_instance': 1,
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1494': {
        'id': 475,
        'name': 'GRID A100-2-10C',
        'ATTR_LIKE': '0x20B0:0x1470',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1495': {
        'id': 476,
        'name': 'GRID A100-3-20C',
        'ATTR_LIKE': '0x20B0:0x1471',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1496': {
        'id': 477,
        'name': 'GRID A100-4-20C',
        'ATTR_LIKE': '0x20B0:0x1472',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20F1:0x1497': {
        'id': 478,
        'name': 'GRID A100-7-40C',
        'ATTR_LIKE': '0x20B0:0x1473',
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1
    },
    '0x20BF:0x4450': {
        'id': 506,
        'name': 'GRID A100B-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x20BF:0x4451': {
        'id': 507,
        'name': 'GRID A100B-5C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
            'framebuffer': '0x128000000',
            'fbReservation': '0x18000000',
        },
    },
    '0x20BF:0x4452': {
        'id': 508,
        'name': 'GRID A100B-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
            'framebuffer': '0x1DC000000',
            'fbReservation': '0x24000000',
        },
    },
    '0x20BF:0x4453': {
        'id': 509,
        'name': 'GRID A100B-10C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
            'framebuffer': '0x254000000',
            'fbReservation': '0x2C000000',
        },
    },
    '0x20BF:0x4454': {
        'id': 510,
        'name': 'GRID A100B-20C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
            'framebuffer': '0x4AC000000',
            'fbReservation': '0x54000000',
        },
    },
    '0x20BF:0x4455': {
        'id': 511,
        'name': 'GRID A100B-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DF6:0x13F1',
        'OVERRIDES': {
            'bar1Length': '0x100',
            'framebuffer': '0x95C000000',
            'fbReservation': '0xA4000000',
            'multiVgpuSupported': 1,
        },
    },
    '0x20BF:0x5560': {
        'id': 517,
        'name': 'GRID A100B-1-5C',
        'ATTR_LIKE': '0x20BF:0x4451',
        'OVERRIDES': {
            'gpuInstanceSize': 1,
            'max_instance': 7,
        },
    },
    '0x20BF:0x5561': {
        'id': 518,
        'name': 'GRID A100B-2-10C',
        'ATTR_LIKE': '0x20BF:0x4453',
        'OVERRIDES': {
            'gpuInstanceSize': 2,
            'max_instance': 3,
        },
    },
    '0x20BF:0x5562': {
        'id': 519,
        'name': 'GRID A100B-3-20C',
        'ATTR_LIKE': '0x20BF:0x4454',
        'OVERRIDES': {
            'gpuInstanceSize': 3,
            'max_instance': 2,
        },
    },
    '0x20BF:0x5563': {
        'id': 520,
        'name': 'GRID A100B-4-20C',
        'ATTR_LIKE': '0x20BF:0x4454',
        'OVERRIDES': {
            'gpuInstanceSize': 4,
            'max_instance': 1,
        },
    },
    '0x20BF:0x5564': {
        'id': 521,
        'name': 'GRID A100B-7-40C',
        'ATTR_LIKE': '0x20BF:0x4455',
        'OVERRIDES': {
            'gpuInstanceSize': 7,
            'max_instance': 1,
            'multiVgpuSupported': 0,
        },
    },
    '0x1EB8:0x1313': {
        'id': 227,
        'name': 'GRID T4-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1EB8:0x1367': {
        'id': 277,
        'name': 'GRID RTX T4-4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1EB8:0x148D': {
        'id': 490,
        'name': 'GRID RTX T4-2',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '2G',
        'ARCH': 'aarch64',
    },
    '0x1EB8:0x148E': {
        'id': 491,
        'name': 'GRID RTX T4-1',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '1G',
        'ARCH': 'aarch64',
    },
    '0x1EB8:0x148F': {
        'id': 492,
        'name': 'GRID RTX T4-0',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'ARCH': 'aarch64',
    },
    '0x1E37:0x136A': {
        'id': 280,
        'name': 'GRID RTX T10-4',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1E37:0x148A': {
        'id': 493,
        'name': 'GRID RTX T10-2',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '2G',
        'ARCH': 'aarch64',
    },
    '0x1E37:0x148B': {
        'id': 494,
        'name': 'GRID RTX T10-1',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '1G',
        'ARCH': 'aarch64',
    },
    '0x1E37:0x148C': {
        'id': 495,
        'name': 'GRID RTX T10-0',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': 'HALFG',
        'ARCH': 'aarch64',
    },
    '0x1E37:0x13A8': {
        'id': 323,
        'name': 'GRID RTX T10x-4',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '4G',
        'ARCH': 'amd64',
    },
    '0x1E37:0x13A4': {
        'id': 325,
        'name': 'GeForce RTX T10-4',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1E37:0x1348': {
        'id': 236,
        'name': 'GeForce RTX T10x-4',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '4G',
    },
    '0x1E30:0x1328': {
        'id': 259,
        'name': 'GRID RTX6000-4Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1E30:0x13BF': {
        'id': 343,
        'name': 'GRID RTX6000-4C',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x1E30:0x1330': {
        'id': 267,
        'name': 'GRID RTX8000-4Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1E30:0x13C4': {
        'id': 348,
        'name': 'GRID RTX8000-4C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x100',
            'max_instance': 8,
        },
    },
    '0x1DF6:0x13E7': {
        'id': 357,
        'name': 'GRID V100S-4Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1DF6:0x13F1': {
        'id': 361,
        'name': 'GRID V100S-4C',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1DF6:0x13ED': {
        'id': 367,
        'name': 'GRID V100S-4A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1E78:0x13FC': {
        'id': 378,
        'name': 'GRID RTX6000P-4Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1E78:0x140D': {
        'id': 387,
        'name': 'GRID RTX6000P-4C',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
    },
    '0x1E78:0x1404': {
        'id': 395,
        'name': 'GRID RTX6000P-4A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1E30:0x143C': {
        'id': 440,
        'name': 'GRID RTX6000-4A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1E78:0x1417': {
        'id': 407,
        'name': 'GRID RTX8000P-4Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x1E78:0x142B': {
        'id': 427,
        'name': 'GRID RTX8000P-4C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'max_instance': 8,
        },
    },
    '0x1E78:0x1421': {
        'id': 417,
        'name': 'GRID RTX8000P-4A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x1E30:0x1446': {
        'id': 450,
        'name': 'GRID RTX8000-4A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    #
    # 6 GB Profiles
    #
    '0x1B38:0x11EC': {
        'id': 50,
        'name': 'GRID P40-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '6G',
        'OVERRIDES': {
            'maxPixels': 58982400,
        },
    },
    '0x1B38:0x12B3': {
        'id': 179,
        'name': 'GeForce GTX P40-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '6G',
    },
    '0x1B38:0x1382': {
        'id': 284,
        'name': 'GRID P40-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '6G',
        'OVERRIDES': {
            'bar1Length': '0x2000',
        },
    },
    '0x1B38:0x11F4': {
        'id': 58,
        'name': 'GRID P40-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '6G',
    },
    '0x1B38:0x13B0': {
        'id': 328,
        'name': 'GRID GTX P40-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '6G',
        'ARCH': 'amd64',
    },
    '0x15F7:0x1269': {
        'id': 147,
        'name': 'GRID P100C-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x15F7:0x138D': {
        'id': 306,
        'name': 'GRID P100C-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
    },
    '0x15F7:0x126E': {
        'id': 152,
        'name': 'GRID P100C-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    '0x1E30:0x1329': {
        'id': 260,
        'name': 'GRID RTX6000-6Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x1E30:0x13B9': {
        'id': 331,
        'name': 'GRID RTX6000-6',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '6G',
        'ARCH': 'amd64',
    },
    '0x1E30:0x13C0': {
        'id': 344,
        'name': 'GRID RTX6000-6C',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x1E30:0x1331': {
        'id': 268,
        'name': 'GRID RTX8000-6Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x1E30:0x13C5': {
        'id': 349,
        'name': 'GRID RTX8000-6C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x1E78:0x13FD': {
        'id': 379,
        'name': 'GRID RTX6000P-6Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x1E78:0x1409': {
        'id': 383,
        'name': 'GRID RTX6000P-6',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '6G',
        'ARCH': 'amd64',
    },
    '0x1E78:0x140E': {
        'id': 388,
        'name': 'GRID RTX6000P-6C',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
    },
    '0x1E78:0x1405': {
        'id': 396,
        'name': 'GRID RTX6000P-6A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    '0x1E30:0x143D': {
        'id': 441,
        'name': 'GRID RTX6000-6A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    '0x1E78:0x1418': {
        'id': 408,
        'name': 'GRID RTX8000P-6Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x1E78:0x142C': {
        'id': 428,
        'name': 'GRID RTX8000P-6C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        }
    },
    '0x1E78:0x1422': {
        'id': 418,
        'name': 'GRID RTX8000P-6A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    '0x1E30:0x1447': {
        'id': 451,
        'name': 'GRID RTX8000-6A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    #
    # 8 GB Profiles
    #
    '0x13F2:0x11B1': {
        'id': 21,
        'name': 'GRID M60-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x13F2:0x1150': {
        'id': 22,
        'name': 'GRID M60-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '8G',
        'OVERRIDES': {
            'display_width': 5120,
            'display_height': 2880,
            'maxPixels': 35389440,
            'multiVgpuSupported': 1,
        },
    },
    '0x13F3:0x11AD': {
        'id': 33,
        'name': 'GRID M6-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
    },
    '0x13F3:0x1184': {
        'id': 34,
        'name': 'GRID M6-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x1150',  # M60-8Q
    },
    '0x13BD:0x11D6': {
        'id': 44,
        'name': 'GRID M10-8A',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
    },
    '0x13BD:0x11D2': {
        'id': 45,
        'name': 'GRID M10-8Q',
        'PGPU_SSID': '0x1160',
        'ATTR_LIKE': '0x13F2:0x1150',  # M60-8Q
        'OVERRIDES': {
            'eccSupported': 0,
        },
    },
    '0x1B38:0x11ED': {
        'id': 51,
        'name': 'GRID P40-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1B38:0x1383': {
        'id': 285,
        'name': 'GRID P40-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '8G',
        'OVERRIDES': {
            'bar1Length': '0x2000',
        },
    },
    '0x1B38:0x11F5': {
        'id': 59,
        'name': 'GRID P40-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1B38:0x13D0': {
        'id': 342,
        'name': 'GRID GTX P40-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1BB3:0x1207': {
        'id': 66,
        'name': 'GRID P4-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x1BB3:0x1380': {
        'id': 289,
        'name': 'GRID P4-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x100',
            'multiVgpuSupported': 1,
        }
    },
    '0x1BB3:0x120B': {
        'id': 70,
        'name': 'GRID P4-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1BB3:0x136F': {
        'id': 276,
        'name': 'GRID GTX P4-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1BB4:0x11FC': {
        'id': 75,
        'name': 'GRID P6-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1BB4:0x1387': {
        'id': 291,
        'name': 'GRID P6-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1BB4:0x1201': {
        'id': 80,
        'name': 'GRID P6-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x15F8:0x1225': {
        'id': 86,
        'name': 'GRID P100-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x15F8:0x138B': {
        'id': 294,
        'name': 'GRID P100-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x15F8:0x122A': {
        'id': 91,
        'name': 'GRID P100-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x15F9:0x1230': {
        'id': 97,
        'name': 'GRID P100X-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x15F9:0x1389': {
        'id': 297,
        'name': 'GRID P100X-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x15F9:0x1235': {
        'id': 102,
        'name': 'GRID P100X-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1DB4:0x1252': {
        'id': 108,
        'name': 'GRID V100-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DB4:0x1394': {
        'id': 300,
        'name': 'GRID V100-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DB4:0x1257': {
        'id': 113,
        'name': 'GRID V100-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1DB1:0x125D': {
        'id': 119,
        'name': 'GRID V100X-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DB1:0x138F': {
        'id': 303,
        'name': 'GRID V100X-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DB1:0x1262': {
        'id': 124,
        'name': 'GRID V100X-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1DB3:0x1295': {
        'id': 168,
        'name': 'GRID V100L-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DB3:0x1399': {
        'id': 309,
        'name': 'GRID V100L-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DB3:0x129A': {
        'id': 173,
        'name': 'GRID V100L-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1DB6:0x12C2': {
        'id': 183,
        'name': 'GRID V100D-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DB6:0x13CD': {
        'id': 339,
        'name': 'GRID GTX V100D-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1DB6:0x1396': {
        'id': 312,
        'name': 'GRID V100D-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DB6:0x12C8': {
        'id': 189,
        'name': 'GRID V100D-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1DB5:0x12D0': {
        'id': 197,
        'name': 'GRID V100DX-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DB5:0x1391': {
        'id': 316,
        'name': 'GRID V100DX-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DB5:0x12D6': {
        'id': 203,
        'name': 'GRID V100DX-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1EB8:0x130F': {
        'id': 233,
        'name': 'GRID T4-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1EB8:0x139B': {
        'id': 320,
        'name': 'GRID T4-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x1EB8:0x1314': {
        'id': 228,
        'name': 'GRID T4-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1EB8:0x1368': {
        'id': 278,
        'name': 'GRID RTX T4-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1E37:0x136B': {
        'id': 281,
        'name': 'GRID RTX T10-8',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1E37:0x13A9': {
        'id': 324,
        'name': 'GRID RTX T10x-8',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1E37:0x13A5': {
        'id': 326,
        'name': 'GeForce RTX T10-8',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1E37:0x1347': {
        'id': 235,
        'name': 'GeForce RTX T10x-8',
        'PGPU_SSID': '0x1304',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x1E30:0x132A': {
        'id': 261,
        'name': 'GRID RTX6000-8Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1E30:0x13CB': {
        'id': 337,
        'name': 'GRID RTX6000-8',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1E30:0x13C1': {
        'id': 345,
        'name': 'GRID RTX6000-8C',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x1E30:0x1332': {
        'id': 269,
        'name': 'GRID RTX8000-8Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1E30:0x13C6': {
        'id': 350,
        'name': 'GRID RTX8000-8C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x100',
        },
    },
    '0x1DF6:0x13E8': {
        'id': 358,
        'name': 'GRID V100S-8Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1DF6:0x13F2': {
        'id': 362,
        'name': 'GRID V100S-8C',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1DF6:0x13EE': {
        'id': 368,
        'name': 'GRID V100S-8A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1E78:0x13FE': {
        'id': 380,
        'name': 'GRID RTX6000P-8Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1E78:0x140A': {
        'id': 384,
        'name': 'GRID RTX6000P-8',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
        'ARCH': 'amd64',
    },
    '0x1E78:0x140F': {
        'id': 389,
        'name': 'GRID RTX6000P-8C',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
    },
    '0x1E78:0x1406': {
        'id': 397,
        'name': 'GRID RTX6000P-8A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1E30:0x143E': {
        'id': 442,
        'name': 'GRID RTX6000-8A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1E78:0x1419': {
        'id': 409,
        'name': 'GRID RTX8000P-8Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x1E78:0x142D': {
        'id': 429,
        'name': 'GRID RTX8000P-8C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
    },
    '0x1E78:0x1423': {
        'id': 419,
        'name': 'GRID RTX8000P-8A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    '0x1E30:0x1448': {
        'id': 452,
        'name': 'GRID RTX8000-8A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F5',  # P40-8A
    },
    #
    # 12 GB Profiles
    #
    '0x1B38:0x11EE': {
        'id': 52,
        'name': 'GRID P40-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '12G',
    },
    '0x1B38:0x12B2': {
        'id': 178,
        'name': 'GeForce GTX P40-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '12G',
    },
    '0x1B38:0x1384': {
        'id': 286,
        'name': 'GRID P40-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '12G',
        'OVERRIDES': {
            'bar1Length': '0x4000',
        },
    },
    '0x1B38:0x11F6': {
        'id': 60,
        'name': 'GRID P40-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '12G',
    },
    '0x1B38:0x13B1': {
        'id': 329,
        'name': 'GRID GTX P40-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
        'ARCH': 'amd64',
    },
    '0x15F7:0x126A': {
        'id': 148,
        'name': 'GRID P100C-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x15F7:0x137D': {
        'id': 307,
        'name': 'GRID P100C-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x15F7:0x126F': {
        'id': 153,
        'name': 'GRID P100C-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
    },
    '0x1E78:0x1407': {
        'id': 398,
        'name': 'GRID RTX6000P-12A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x143F': {
        'id': 443,
        'name': 'GRID RTX6000-12A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x1424': {
        'id': 420,
        'name': 'GRID RTX8000P-12A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x1449': {
        'id': 453,
        'name': 'GRID RTX8000-12A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x132B': {
        'id': 262,
        'name': 'GRID RTX6000-12Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x13BA': {
        'id': 332,
        'name': 'GRID RTX6000-12',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x13C2': {
        'id': 346,
        'name': 'GRID RTX6000-12C',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
            'bar1Length': '0x100',
        },
    },
    '0x1E30:0x1333': {
        'id': 270,
        'name': 'GRID RTX8000-12Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x13BC': {
        'id': 334,
        'name': 'GRID RTX8000-12',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E30:0x13C7': {
        'id': 351,
        'name': 'GRID RTX8000-12C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
            'bar1Length': '0x100',
        },
    },
    '0x1E78:0x13FF': {
        'id': 381,
        'name': 'GRID RTX6000P-12Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x140B': {
        'id': 385,
        'name': 'GRID RTX6000P-12',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x1410': {
        'id': 390,
        'name': 'GRID RTX6000P-12C',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x141A': {
        'id': 410,
        'name': 'GRID RTX8000P-12Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x1427': {
        'id': 423,
        'name': 'GRID RTX8000P-12',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x1E78:0x142E': {
        'id': 430,
        'name': 'GRID RTX8000P-12C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
            'bar1Length': '0x2000',
        },
    },
    #
    # 16 GB Profiles
    #
    '0x1BB4:0x11FD': {
        'id': 76,
        'name': 'GRID P6-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '16G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x1BB4:0x137F': {
        'id': 292,
        'name': 'GRID P6-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '16G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x4000',
        },
    },
    '0x1BB4:0x1202': {
        'id': 81,
        'name': 'GRID P6-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '16G',
    },
    '0x15F8:0x1226': {
        'id': 87,
        'name': 'GRID P100-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
    },
    '0x15F8:0x137C': {
        'id': 295,
        'name': 'GRID P100-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
    },
    '0x15F8:0x122B': {
        'id': 92,
        'name': 'GRID P100-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x15F9:0x1231': {
        'id': 98,
        'name': 'GRID P100X-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'nvlinkP2PSupported': 1
    },
    '0x15F9:0x137B': {
        'id': 298,
        'name': 'GRID P100X-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'nvlinkP2PSupported': 1
    },
    '0x15F9:0x1236': {
        'id': 103,
        'name': 'GRID P100X-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1DB4:0x1253': {
        'id': 109,
        'name': 'GRID V100-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
    },
    '0x1DB4:0x1379': {
        'id': 301,
        'name': 'GRID V100-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
    },
    '0x1DB4:0x1258': {
        'id': 114,
        'name': 'GRID V100-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1DB1:0x125E': {
        'id': 120,
        'name': 'GRID V100X-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'nvlinkP2PSupported': 1,
    },
    '0x1DB1:0x1378': {
        'id': 304,
        'name': 'GRID V100X-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'nvlinkP2PSupported': 1,
    },
    '0x1DB1:0x1263': {
        'id': 125,
        'name': 'GRID V100X-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1DB3:0x1296': {
        'id': 169,
        'name': 'GRID V100L-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
    },
    '0x1DB3:0x137A': {
        'id': 310,
        'name': 'GRID V100L-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
    },
    '0x1DB3:0x129B': {
        'id': 174,
        'name': 'GRID V100L-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1DB6:0x12C3': {
        'id': 184,
        'name': 'GRID V100D-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'OVERRIDES': {
            'multiVgpuSupported': 0,
        },
    },
    '0x1DB6:0x13CE': {
        'id': 340,
        'name': 'GRID GTX V100D-16',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '16G',
        'ARCH': 'amd64',
    },
    '0x1DB6:0x1397': {
        'id': 313,
        'name': 'GRID V100D-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'OVERRIDES': {
            'multiVgpuSupported': 0,
        },
    },
    '0x1DB6:0x12C9': {
        'id': 190,
        'name': 'GRID V100D-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1DB5:0x12D1': {
        'id': 198,
        'name': 'GRID V100DX-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DB6:0x12C3',  # V100D-16Q
    },
    '0x1DB5:0x1392': {
        'id': 317,
        'name': 'GRID V100DX-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DB6:0x1397',  # V100D-16C
    },
    '0x1DB5:0x12D7': {
        'id': 204,
        'name': 'GRID V100DX-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1EB8:0x1369': {
        'id': 279,
        'name': 'GRID RTX T4-16',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '16G',
        'OVERRIDES': {
            'framebuffer': '0x3BA400000',
            'fbReservation': '0x45C00000',
        },
    },
    '0x1E37:0x136C': {
        'id': 282,
        'name': 'GRID RTX T10-16',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '16G',
    },
    '0x1E37:0x13A6': {
        'id': 327,
        'name': 'GeForce RTX T10-16',
        'PGPU_SSID': '0x1370',
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '16G',
    },
    '0x1DF6:0x13E9': {
        'id': 359,
        'name': 'GRID V100S-16Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1DB6:0x12C3',  # V100D-16Q
    },
    '0x1DF6:0x13F3': {
        'id': 363,
        'name': 'GRID V100S-16C',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1DB6:0x1397',  # V100D-16C
    },
    '0x1DF6:0x13EF': {
        'id': 369,
        'name': 'GRID V100S-16A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
    },
    '0x1EB8:0x1310': {
        'id': 234,
        'name': 'GRID T4-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'OVERRIDES': {
            'framebuffer': '0x3BA400000',
            'fbReservation': '0x45C00000',
        },
    },
    '0x1EB8:0x1375': {
        'id': 321,
        'name': 'GRID T4-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'OVERRIDES': {
            'framebuffer': '0x3BA400000',
            'fbReservation': '0x45C00000',
            'bar1Length': '0x100',
        },
    },
    '0x1EB8:0x1315': {
        'id': 229,
        'name': 'GRID T4-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
        'OVERRIDES': {
            'framebuffer': '0x3BA400000',
            'fbReservation': '0x45C00000',
        },
    },
    '0x1E30:0x1334': {
        'id': 271,
        'name': 'GRID RTX8000-16Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1DB6:0x12C3',  # V100D-16Q
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x1E30:0x13CC': {
        'id': 338,
        'name': 'GRID RTX8000-16',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '16G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x1E30:0x13C8': {
        'id': 352,
        'name': 'GRID RTX8000-16C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1DB6:0x1397',  # V100D-16C
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
            'bar1Length': '0x100',
        },
    },
    '0x1E78:0x141B': {
        'id': 411,
        'name': 'GRID RTX8000P-16Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1DB6:0x12C3',  # V100D-16Q
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x1E78:0x1428': {
        'id': 424,
        'name': 'GRID RTX8000P-16',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '16G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x1E78:0x142F': {
        'id': 431,
        'name': 'GRID RTX8000P-16C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1DB6:0x1397',  # V100D-16C
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
            'bar1Length': '0x2000',
        },
    },
    '0x1E78:0x1436': {
        'id': 434,
        'name': 'GRID RTX8000P-16A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x1E30:0x144A': {
        'id': 454,
        'name': 'GRID RTX8000-16A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    #
    # 24 GB Profiles
    #
    '0x1B38:0x11EF': {
        'id': 53,
        'name': 'GRID P40-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x1B38:0x12B1': {
        'id': 177,
        'name': 'GeForce GTX P40-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'NGN_ATTRIBUTES',
        'FB_LIKE': '24G',
    },
    '0x1B38:0x137E': {
        'id': 287,
        'name': 'GRID P40-24C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x8000',
        },
    },
    '0x1B38:0x11F7': {
        'id': 61,
        'name': 'GRID P40-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '24G',
    },
    '0x1B38:0x13B2': {
        'id': 330,
        'name': 'GRID GTX P40-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
        'ARCH': 'amd64',
    },
    '0x1E78:0x1408': {
        'id': 399,
        'name': 'GRID RTX6000P-24A',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
        },
    },
    '0x1E30:0x1440': {
        'id': 444,
        'name': 'GRID RTX6000-24A',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
        },
    },
    '0x1E78:0x1425': {
        'id': 421,
        'name': 'GRID RTX8000P-24A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'framebuffer': '0x596000000',
            'fbReservation': '0x6A000000',
        },
    },
    '0x1E30:0x144B': {
        'id': 455,
        'name': 'GRID RTX8000-24A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'framebuffer': '0x596000000',
            'fbReservation': '0x6A000000',
        },
    },
    '0x1E30:0x132C': {
        'id': 263,
        'name': 'GRID RTX6000-24Q',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
        },
        'nvlinkP2PSupported': 1,
    },
    '0x1E30:0x13BB': {
        'id': 333,
        'name': 'GRID RTX6000-24',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
        },
    },
    '0x1E30:0x13C3': {
        'id': 347,
        'name': 'GRID RTX6000-24C',
        'PGPU_SSID': '0x12BA',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
            'bar1Length': '0x100',
        },
    },
    '0x1E78:0x1400': {
        'id': 382,
        'name': 'GRID RTX6000P-24Q',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1E30:0x132C',  # RTX6000-24Q
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x1E78:0x140C': {
        'id': 386,
        'name': 'GRID RTX6000P-24',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x595800000',
            'fbReservation': '0x6A800000',
        },
    },
    '0x1E78:0x1411': {
        'id': 391,
        'name': 'GRID RTX6000P-24C',
        'PGPU_SSID': '0x13D9',
        'ATTR_LIKE': '0x1E30:0x13C3',  # RTX6000-24C
        'OVERRIDES': {
            'bar1Length': '0x8000',
        }
    },
    '0x1E30:0x1335': {
        'id': 272,
        'name': 'GRID RTX8000-24Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1E30:0x132C',  # RTX6000-24Q
        'OVERRIDES': {
            'framebuffer': '0x596000000',
            'fbReservation': '0x6A000000',
            'multiVgpuSupported': 0,
            'nvlinkP2PSupported': 0,
        },
    },
    '0x1E30:0x13BD': {
        'id': 335,
        'name': 'GRID RTX8000-24',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0x596000000',
            'fbReservation': '0x6A000000',
        },
    },
    '0x1E30:0x13C9': {
        'id': 353,
        'name': 'GRID RTX8000-24C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'framebuffer': '0x596000000',
            'fbReservation': '0x6A000000',
            'bar1Length': '0x100',
        },
    },
    '0x1E78:0x141C': {
        'id': 412,
        'name': 'GRID RTX8000P-24Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x1335',  # RTX8000-24Q
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x1E78:0x1429': {
        'id': 425,
        'name': 'GRID RTX8000P-24',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x13BD',  # RTX8000-24
    },
    '0x1E78:0x1430': {
        'id': 432,
        'name': 'GRID RTX8000P-24C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x13C9',  # RTX8000-24C
        'OVERRIDES': {
            'bar1Length': '0x4000',
        }
    },
    '0x2237:0x155E': {
        'id': 653,
        'name': 'NVIDIA A10G-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '6G',
        'gpuDirectSupported': 1
    },
    '0x2237:0x155F': {
        'id': 654,
        'name': 'NVIDIA A10G-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '8G',
        'gpuDirectSupported': 1
    },
    '0x2237:0x1560': {
        'id': 655,
        'name': 'NVIDIA A10G-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '12G',
        'gpuDirectSupported': 1
    },
    '0x2237:0x1561': {
        'id': 656,
        'name': 'NVIDIA A10G-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '24G',
        'gpuDirectSupported': 1
    },
    '0x2237:0x162A': {
        'id': 724,
        'name': 'NVIDIA A10G-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x2237:0x162B': {
        'id': 725,
        'name': 'NVIDIA A10G-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x2237:0x162C': {
        'id': 726,
        'name': 'NVIDIA A10G-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x2237:0x162D': {
        'id': 727,
        'name': 'NVIDIA A10G-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x2237:0x162E': {
        'id': 728,
        'name': 'NVIDIA A10G-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
    },
    '0x2237:0x162F': {
        'id': 729,
        'name': 'NVIDIA A10G-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x2237:0x1630': {
        'id': 730,
        'name': 'NVIDIA A10G-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
    },
    '0x2237:0x1631': {
        'id': 731,
        'name': 'NVIDIA A10G-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
    },
    '0x2237:0x1632': {
        'id': 732,
        'name': 'NVIDIA A10G-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
    },
    '0x2237:0x1633': {
        'id': 733,
        'name': 'NVIDIA A10G-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
    },
    '0x2237:0x1634': {
        'id': 734,
        'name': 'NVIDIA A10G-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x2237:0x1635': {
        'id': 735,
        'name': 'NVIDIA A10G-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
    },
    '0x2237:0x1636': {
        'id': 736,
        'name': 'NVIDIA A10G-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
    },
    '0x2237:0x1637': {
        'id': 737,
        'name': 'NVIDIA A10G-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
    },
    '0x2237:0x1638': {
        'id': 738,
        'name': 'NVIDIA A10G-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
    },
    '0x2237:0x1639': {
        'id': 739,
        'name': 'NVIDIA A10G-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
    },
    '0x2237:0x163A': {
        'id': 740,
        'name': 'NVIDIA A10G-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
    },
    '0x2237:0x163B': {
        'id': 741,
        'name': 'NVIDIA A10G-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
    },
    '0x2231:0x1562': {
        'id': 657,
        'name': 'NVIDIA RTXA5000-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1563': {
        'id': 658,
        'name': 'NVIDIA RTXA5000-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1564': {
        'id': 659,
        'name': 'NVIDIA RTXA5000-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1565': {
        'id': 660,
        'name': 'NVIDIA RTXA5000-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1566': {
        'id': 661,
        'name': 'NVIDIA RTXA5000-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1567': {
        'id': 662,
        'name': 'NVIDIA RTXA5000-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1568': {
        'id': 663,
        'name': 'NVIDIA RTXA5000-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1569': {
        'id': 664,
        'name': 'NVIDIA RTXA5000-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x156A': {
        'id': 665,
        'name': 'NVIDIA RTXA5000-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x156B': {
        'id': 666,
        'name': 'NVIDIA RTXA5000-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x100',
        },
        'nvlinkP2PSupported': 1,
    },
    '0x2231:0x156C': {
        'id': 667,
        'name': 'NVIDIA RTXA5000-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x156D': {
        'id': 668,
        'name': 'NVIDIA RTXA5000-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x156E': {
        'id': 669,
        'name': 'NVIDIA RTXA5000-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x156F': {
        'id': 670,
        'name': 'NVIDIA RTXA5000-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1570': {
        'id': 671,
        'name': 'NVIDIA RTXA5000-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1571': {
        'id': 672,
        'name': 'NVIDIA RTXA5000-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1572': {
        'id': 673,
        'name': 'NVIDIA RTXA5000-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1573': {
        'id': 674,
        'name': 'NVIDIA RTXA5000-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2231:0x1578': {
        'id': 675,
        'name': 'NVIDIA RTXA5000-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2231:0x1579': {
        'id': 676,
        'name': 'NVIDIA RTXA5000-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2231:0x157A': {
        'id': 677,
        'name': 'NVIDIA RTXA5000-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2231:0x157B': {
        'id': 678,
        'name': 'NVIDIA RTXA5000-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2231:0x157C': {
        'id': 679,
        'name': 'NVIDIA RTXA5000-24C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1
    },
    '0x2231:0x1574': {
        'id': 680,
        'name': 'NVIDIA RTXA5000-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '6G',
    },
    '0x2231:0x1575': {
        'id': 681,
        'name': 'NVIDIA RTXA5000-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x2231:0x1576': {
        'id': 682,
        'name': 'NVIDIA RTXA5000-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
    },
    '0x2231:0x1577': {
        'id': 683,
        'name': 'NVIDIA RTXA5000-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
    },
    '0x2233:0x165C': {
        'id': 760,
        'name': 'NVIDIA RTXA5500-1B',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x165D': {
        'id': 761,
        'name': 'NVIDIA RTXA5500-2B',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x165E': {
        'id': 762,
        'name': 'NVIDIA RTXA5500-1Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x165F': {
        'id': 763,
        'name': 'NVIDIA RTXA5500-2Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1660': {
        'id': 764,
        'name': 'NVIDIA RTXA5500-3Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1661': {
        'id': 765,
        'name': 'NVIDIA RTXA5500-4Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1662': {
        'id': 766,
        'name': 'NVIDIA RTXA5500-6Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1663': {
        'id': 767,
        'name': 'NVIDIA RTXA5500-8Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1664': {
        'id': 768,
        'name': 'NVIDIA RTXA5500-12Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1665': {
        'id': 769,
        'name': 'NVIDIA RTXA5500-24Q',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x100',
        },
        'nvlinkP2PSupported': 1,
    },
    '0x2233:0x1666': {
        'id': 770,
        'name': 'NVIDIA RTXA5500-1A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1667': {
        'id': 771,
        'name': 'NVIDIA RTXA5500-2A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1668': {
        'id': 772,
        'name': 'NVIDIA RTXA5500-3A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x1669': {
        'id': 773,
        'name': 'NVIDIA RTXA5500-4A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x166A': {
        'id': 774,
        'name': 'NVIDIA RTXA5500-6A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x166B': {
        'id': 775,
        'name': 'NVIDIA RTXA5500-8A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x166C': {
        'id': 776,
        'name': 'NVIDIA RTXA5500-12A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x166D': {
        'id': 777,
        'name': 'NVIDIA RTXA5500-24A',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2233:0x166E': {
        'id': 778,
        'name': 'NVIDIA RTXA5500-6',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '6G',
    },
    '0x2233:0x166F': {
        'id': 779,
        'name': 'NVIDIA RTXA5500-8',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '8G',
    },
    '0x2233:0x1670': {
        'id': 780,
        'name': 'NVIDIA RTXA5500-12',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '12G',
    },
    '0x2233:0x1671': {
        'id': 781,
        'name': 'NVIDIA RTXA5500-24',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '24G',
    },
    '0x2233:0x1672': {
        'id': 782,
        'name': 'NVIDIA RTXA5500-4C',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2233:0x1673': {
        'id': 783,
        'name': 'NVIDIA RTXA5500-6C',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2233:0x1674': {
        'id': 784,
        'name': 'NVIDIA RTXA5500-8C',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2233:0x1675': {
        'id': 785,
        'name': 'NVIDIA RTXA5500-12C',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2233:0x1676': {
        'id': 786,
        'name': 'NVIDIA RTXA5500-24C',
        'PGPU_SSID': '0x165A',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
        'nvlinkP2PSupported': 1,
    },
    #
    # 32 GB Profiles
    #
    '0x1DB6:0x12C4': {
        'id': 185,
        'name': 'GRID V100D-32Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '32G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x1DB6:0x13CF': {
        'id': 341,
        'name': 'GRID GTX V100D-32',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '32G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x1DB6:0x1377': {
        'id': 314,
        'name': 'GRID V100D-32C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '32G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x8000',
        },
    },
    '0x1DB6:0x12CA': {
        'id': 191,
        'name': 'GRID V100D-32A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '32G',
    },
    '0x1DB5:0x12D2': {
        'id': 199,
        'name': 'GRID V100DX-32Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DB6:0x12C4',  # V100D-32Q
        'nvlinkP2PSupported': 1,
    },
    '0x1DB5:0x1376': {
        'id': 318,
        'name': 'GRID V100DX-32C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DB6:0x1377',  # V100D-32C
        'nvlinkP2PSupported': 1
    },
    '0x1DB5:0x12D8': {
        'id': 205,
        'name': 'GRID V100DX-32A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1DB6:0x12CA',  # V100D-32A
    },
    '0x1DF6:0x13EA': {
        'id': 360,
        'name': 'GRID V100S-32Q',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1DB6:0x12C4',  # V100D-32Q
    },
    '0x1DF6:0x13F4': {
        'id': 364,
        'name': 'GRID V100S-32C',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1DB6:0x1377',  # V100D-32C
    },
    '0x1DF6:0x13F0': {
        'id': 370,
        'name': 'GRID V100S-32A',
        'PGPU_SSID': '0x13D6',
        'ATTR_LIKE': '0x1DB6:0x12CA',  # V100D-32A
    },
    #
    # 48 GB Profiles
    #
    '0x1E30:0x1336': {
        'id': 273,
        'name': 'GRID RTX8000-48Q',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'framebuffer': '0xB2D200000',
            'fbReservation': '0xD2E00000',
        },
        'nvlinkP2PSupported': 1,
    },
    '0x1E30:0x13BE': {
        'id': 336,
        'name': 'GRID RTX8000-48',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '48G',
        'ARCH': 'amd64',
        'OVERRIDES': {
            'framebuffer': '0xB2D200000',
            'fbReservation': '0xD2E00000',
        },
    },
    '0x1E30:0x13CA': {
        'id': 354,
        'name': 'GRID RTX8000-48C',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x100',
            'framebuffer': '0xB2D200000',
            'fbReservation': '0xD2E00000',
        },
    },
    '0x1E78:0x141D': {
        'id': 413,
        'name': 'GRID RTX8000P-48Q',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x1336',  # RTX8000-48Q
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x1E78:0x142A': {
        'id': 426,
        'name': 'GRID RTX8000P-48',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x13BE',  # RTX8000-48
    },
    '0x1E78:0x1431': {
        'id': 433,
        'name': 'GRID RTX8000P-48C',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': '0x1E30:0x13CA',  # RTX8000-48C
        'OVERRIDES': {
            'bar1Length': '0x8000',
        }
    },
    '0x1E78:0x1426': {
        'id': 422,
        'name': 'GRID RTX8000P-48A',
        'PGPU_SSID': '0x13D8',
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'framebuffer': '0xB2D200000',
            'fbReservation': '0xD2E00000',
        },
    },
    '0x1E30:0x144C': {
        'id': 456,
        'name': 'GRID RTX8000-48A',
        'PGPU_SSID': '0x129E',
        'ATTR_LIKE': '0x1E78:0x1426',  # GRID RTX8000P-48A
    },
    '0x2230:0x14FA': {
        'id': 522,
        'name': 'NVIDIA RTXA6000-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x14FB': {
        'id': 523,
        'name': 'NVIDIA RTXA6000-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x14FC': {
        'id': 524,
        'name': 'NVIDIA RTXA6000-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x14FD': {
        'id': 525,
        'name': 'NVIDIA RTXA6000-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x14FE': {
        'id': 526,
        'name': 'NVIDIA RTXA6000-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x14FF': {
        'id': 527,
        'name': 'NVIDIA RTXA6000-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1500': {
        'id': 528,
        'name': 'NVIDIA RTXA6000-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1501': {
        'id': 529,
        'name': 'NVIDIA RTXA6000-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1502': {
        'id': 530,
        'name': 'NVIDIA RTXA6000-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1503': {
        'id': 531,
        'name': 'NVIDIA RTXA6000-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1504': {
        'id': 532,
        'name': 'NVIDIA RTXA6000-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1505': {
        'id': 533,
        'name': 'NVIDIA RTXA6000-48Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x100',
        },
        'nvlinkP2PSupported': 1
    },
    '0x2230:0x1506': {
        'id': 534,
        'name': 'NVIDIA RTXA6000-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1507': {
        'id': 535,
        'name': 'NVIDIA RTXA6000-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1508': {
        'id': 536,
        'name': 'NVIDIA RTXA6000-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1509': {
        'id': 537,
        'name': 'NVIDIA RTXA6000-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150A': {
        'id': 538,
        'name': 'NVIDIA RTXA6000-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150B': {
        'id': 539,
        'name': 'NVIDIA RTXA6000-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150C': {
        'id': 540,
        'name': 'NVIDIA RTXA6000-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150D': {
        'id': 541,
        'name': 'NVIDIA RTXA6000-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150E': {
        'id': 542,
        'name': 'NVIDIA RTXA6000-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x150F': {
        'id': 543,
        'name': 'NVIDIA RTXA6000-48A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2230:0x1510': {
        'id': 544,
        'name': 'NVIDIA RTXA6000-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '12G',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
    },
    '0x2230:0x1511': {
        'id': 545,
        'name': 'NVIDIA RTXA6000-16',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '16G',
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
    },
    '0x2230:0x1512': {
        'id': 546,
        'name': 'NVIDIA RTXA6000-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '24G',
    },
    '0x2230:0x1513': {
        'id': 547,
        'name': 'NVIDIA RTXA6000-48',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '48G',
    },
    '0x2230:0x1514': {
        'id': 548,
        'name': 'NVIDIA RTXA6000-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x1515': {
        'id': 549,
        'name': 'NVIDIA RTXA6000-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x1516': {
        'id': 550,
        'name': 'NVIDIA RTXA6000-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x1517': {
        'id': 551,
        'name': 'NVIDIA RTXA6000-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x1518': {
        'id': 552,
        'name': 'NVIDIA RTXA6000-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x1519': {
        'id': 553,
        'name': 'NVIDIA RTXA6000-24C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2230:0x151A': {
        'id': 554,
        'name': 'NVIDIA RTXA6000-48C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14D5': {
        'id': 555,
        'name': 'NVIDIA A40-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14D6': {
        'id': 556,
        'name': 'NVIDIA A40-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14D7': {
        'id': 557,
        'name': 'NVIDIA A40-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14D8': {
        'id': 558,
        'name': 'NVIDIA A40-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14D9': {
        'id': 559,
        'name': 'NVIDIA A40-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DA': {
        'id': 560,
        'name': 'NVIDIA A40-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DB': {
        'id': 561,
        'name': 'NVIDIA A40-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DC': {
        'id': 562,
        'name': 'NVIDIA A40-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DD': {
        'id': 563,
        'name': 'NVIDIA A40-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DE': {
        'id': 564,
        'name': 'NVIDIA A40-16Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x11FD',  # P6-16Q
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14DF': {
        'id': 565,
        'name': 'NVIDIA A40-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E0': {
        'id': 566,
        'name': 'NVIDIA A40-48Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x100',
        },
        'nvlinkP2PSupported': 1
    },
    '0x2235:0x14E1': {
        'id': 567,
        'name': 'NVIDIA A40-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E2': {
        'id': 568,
        'name': 'NVIDIA A40-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E3': {
        'id': 569,
        'name': 'NVIDIA A40-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E4': {
        'id': 570,
        'name': 'NVIDIA A40-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E5': {
        'id': 571,
        'name': 'NVIDIA A40-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E6': {
        'id': 572,
        'name': 'NVIDIA A40-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E7': {
        'id': 573,
        'name': 'NVIDIA A40-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E8': {
        'id': 574,
        'name': 'NVIDIA A40-16A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x1202',  # P6-16A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14E9': {
        'id': 575,
        'name': 'NVIDIA A40-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14EA': {
        'id': 576,
        'name': 'NVIDIA A40-48A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2235:0x14EB': {
        'id': 577,
        'name': 'NVIDIA A40-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '12G',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
        'gpuDirectSupported': 1
    },
    '0x2235:0x14EC': {
        'id': 578,
        'name': 'NVIDIA A40-16',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '16G',
        'OVERRIDES': {
            'framebuffer': '0x3B8000000',
            'fbReservation': '0x48000000',
        },
        'gpuDirectSupported': 1
    },
    '0x2235:0x14ED': {
        'id': 579,
        'name': 'NVIDIA A40-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '24G',
        'gpuDirectSupported': 1
    },
    '0x2235:0x14EE': {
        'id': 580,
        'name': 'NVIDIA A40-48',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '48G',
        'gpuDirectSupported': 1
    },
    '0x2235:0x14F3': {
        'id': 581,
        'name': 'NVIDIA A40-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F4': {
        'id': 582,
        'name': 'NVIDIA A40-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F5': {
        'id': 583,
        'name': 'NVIDIA A40-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F6': {
        'id': 584,
        'name': 'NVIDIA A40-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F7': {
        'id': 585,
        'name': 'NVIDIA A40-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1BB4:0x137F',  # P6-16C
        'OVERRIDES': {
            'multiVgpuSupported': 0,
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F8': {
        'id': 586,
        'name': 'NVIDIA A40-24C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2235:0x14F9': {
        'id': 587,
        'name': 'NVIDIA A40-48C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '48G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1
    },
    '0x2236:0x14B6': {
        'id': 588,
        'name': 'NVIDIA A10-1B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14B7': {
        'id': 589,
        'name': 'NVIDIA A10-2B',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14B8': {
        'id': 590,
        'name': 'NVIDIA A10-1Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14B9': {
        'id': 591,
        'name': 'NVIDIA A10-2Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BA': {
        'id': 592,
        'name': 'NVIDIA A10-3Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EA',  # P40-3Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BB': {
        'id': 593,
        'name': 'NVIDIA A10-4Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BC': {
        'id': 594,
        'name': 'NVIDIA A10-6Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EC',  # P40-6Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BD': {
        'id': 595,
        'name': 'NVIDIA A10-8Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11ED',  # P40-8Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BE': {
        'id': 596,
        'name': 'NVIDIA A10-12Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EE',  # P40-12Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14BF': {
        'id': 597,
        'name': 'NVIDIA A10-24Q',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11EF',  # P40-24Q
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C0': {
        'id': 598,
        'name': 'NVIDIA A10-1A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C1': {
        'id': 599,
        'name': 'NVIDIA A10-2A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C2': {
        'id': 600,
        'name': 'NVIDIA A10-3A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F2',  # P40-3A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C3': {
        'id': 601,
        'name': 'NVIDIA A10-4A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B0',  # M60-4A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C4': {
        'id': 602,
        'name': 'NVIDIA A10-6A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F4',  # P40-6A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C5': {
        'id': 603,
        'name': 'NVIDIA A10-8A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x13F2:0x11B1',  # M60-8A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C6': {
        'id': 604,
        'name': 'NVIDIA A10-12A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F6',  # P40-12A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C7': {
        'id': 605,
        'name': 'NVIDIA A10-24A',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x11F7',  # P40-24A
        'OVERRIDES': {
            'bar1Length': '0x100',
        }
    },
    '0x2236:0x14C8': {
        'id': 606,
        'name': 'NVIDIA A10-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '6G',
        'gpuDirectSupported': 1
    },
    '0x2236:0x14C9': {
        'id': 607,
        'name': 'NVIDIA A10-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '8G',
        'gpuDirectSupported': 1
    },
    '0x2236:0x14CA': {
        'id': 608,
        'name': 'NVIDIA A10-12',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '12G',
        'OVERRIDES': {
            'framebuffer': '0x2CA000000',
            'fbReservation': '0x36000000',
        },
        'gpuDirectSupported': 1
    },
    '0x2236:0x14CB': {
        'id': 609,
        'name': 'NVIDIA A10-24',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
        'gpuDirectSupported': 1
    },
    '0x2236:0x14D0': {
        'id': 610,
        'name': 'NVIDIA A10-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2236:0x14D1': {
        'id': 611,
        'name': 'NVIDIA A10-6C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2236:0x14D2': {
        'id': 612,
        'name': 'NVIDIA A10-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2236:0x14D3': {
        'id': 613,
        'name': 'NVIDIA A10-12C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2236:0x14D4': {
        'id': 614,
        'name': 'NVIDIA A10-24C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1
    },
    '0x20B2:0x1528': {
        'id': 615,
        'name': 'GRID A100DX-4C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1474',  # GRID A100X-4C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
    },
    '0x20B2:0x1529': {
        'id': 616,
        'name': 'GRID A100DX-8C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1476',  # GRID A100X-8C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
    },
    '0x20B2:0x152A': {
        'id': 617,
        'name': 'GRID A100DX-10C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1477',  # GRID A100X-10C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
    },
    '0x20B2:0x152B': {
        'id': 618,
        'name': 'GRID A100DX-16C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x1000',
            'framebuffer': '0x3BC000000',
            'fbReservation': '0x44000000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B2:0x152C': {
        'id': 619,
        'name': 'GRID A100DX-20C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1478',  # GRID A100X-20C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B2:0x152D': {
        'id': 620,
        'name': 'GRID A100DX-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B0:0x1479',  # GRID A100X-40C
        'OVERRIDES': {
            'bar1Length': '0x1000',
            'multiVgpuSupported': 0,
        },
    },
    '0x20B2:0x152E': {
        'id': 621,
        'name': 'GRID A100DX-80C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '80G',
        'OVERRIDES': {
            'bar1Length': '0x1000',
            'multiVgpuSupported': 1,
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1,
    },
    '0x20B2:0x1523': {
        'id': 622,
        'name': 'GRID A100DX-1-10C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x152A',  # GRID A100DX-10C
        'OVERRIDES': {
            'gpuInstanceSize': 1,
            'max_instance': 7,
        },
    },
    '0x20B2:0x160D': {
        'id': 705,
        'name': 'GRID A100DX-1-10CME',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x1523',  # GRID A100DX-1-10C
        'DISABLE_ON': ['esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0', ],
        'OVERRIDES': {
            'max_instance': 1,
        },
    },
    '0x20B2:0x1524': {
        'id': 623,
        'name': 'GRID A100DX-2-20C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x152C',  # GRID A100DX-20C
        'OVERRIDES': {
            'gpuInstanceSize': 2,
            'max_instance': 3,
        },
    },
    '0x20B2:0x1525': {
        'id': 624,
        'name': 'GRID A100DX-3-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x152D',  # GRID A100DX-40C
        'OVERRIDES': {
            'gpuInstanceSize': 3,
            'max_instance': 2,
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B2:0x1526': {
        'id': 625,
        'name': 'GRID A100DX-4-40C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x152D',  # GRID A100DX-40C
        'OVERRIDES': {
            'gpuInstanceSize': 4,
            'max_instance': 1,
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B2:0x1527': {
        'id': 626,
        'name': 'GRID A100DX-7-80C',
        'PGPU_SSID': 0,
        'ATTR_LIKE': '0x20B2:0x152E',  # GRID A100DX-80C
        'OVERRIDES': {
            'gpuInstanceSize': 7,
            'max_instance': 1,
            'multiVgpuSupported': 0,
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B5:0x1596': {
        'id': 692,
        'name': 'GRID A100D-4C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1528',  # GRID A100DX-4C
    },
    '0x20B5:0x1597': {
        'id': 693,
        'name': 'GRID A100D-8C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1529',  # GRID A100DX-8C
    },
    '0x20B5:0x1598': {
        'id': 694,
        'name': 'GRID A100D-10C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x152A',  # GRID A100DX-10C
    },
    '0x20B5:0x1599': {
        'id': 695,
        'name': 'GRID A100D-16C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x152B',  # GRID A100DX-16C
    },
    '0x20B5:0x159A': {
        'id': 696,
        'name': 'GRID A100D-20C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x152C',  # GRID A100DX-20C
    },
    '0x20B5:0x159B': {
        'id': 697,
        'name': 'GRID A100D-40C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x152D',  # GRID A100DX-40C
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B5:0x159C': {
        'id': 698,
        'name': 'GRID A100D-80C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x152E',  # GRID A100DX-80C
        'nvlinkP2PSupported': 1,
    },
    '0x20B5:0x1591': {
        'id': 699,
        'name': 'GRID A100D-1-10C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1523',  # GRID A100DX-1-10C
    },
    '0x20B5:0x160F': {
        'id': 707,
        'name': 'GRID A100D-1-10CME',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B5:0x1591',  # GRID A100D-1-10C
        'DISABLE_ON': ['esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0', ],
        'OVERRIDES': {
            'max_instance': 1,
        },
    },
    '0x20B5:0x1592': {
        'id': 700,
        'name': 'GRID A100D-2-20C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1524',  # GRID A100DX-2-20C
    },
    '0x20B5:0x1593': {
        'id': 701,
        'name': 'GRID A100D-3-40C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1525',  # GRID A100DX-3-40C
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B5:0x1594': {
        'id': 702,
        'name': 'GRID A100D-4-40C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1526',  # GRID A100DX-4-40C
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B5:0x1595': {
        'id': 703,
        'name': 'GRID A100D-7-80C',
        'PGPU_SSID': '0x1533',
        'ATTR_LIKE': '0x20B2:0x1527',  # GRID A100DX-7-80C
        'OVERRIDES': {
            'nvlinkP2PSupported': 0,
        },
    },
    '0x20B7:0x158C': {
        'id': 684,
        'name': 'NVIDIA A30-4C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B7:0x158D': {
        'id': 685,
        'name': 'NVIDIA A30-6C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x1B38:0x1382',  # P40-6C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B7:0x158E': {
        'id': 686,
        'name': 'NVIDIA A30-8C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x1B38:0x1383',  # P40-8C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B7:0x158F': {
        'id': 687,
        'name': 'NVIDIA A30-12C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x1B38:0x1384',  # P40-12C
        'OVERRIDES': {
            'bar1Length': '0x1000',
        },
        'gpuDirectSupported': 1,
    },
    '0x20B7:0x1590': {
        'id': 688,
        'name': 'NVIDIA A30-24C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '24G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x1000',
        },
        'nvlinkP2PSupported': 1,
        'gpuDirectSupported': 1,
    },
    '0x20B7:0x1589': {
        'id': 689,
        'name': 'NVIDIA A30-1-6C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x20B7:0x158D',  # NVIDIA A30-6C
        'OVERRIDES': {
            'gpuInstanceSize': 1,
            'max_instance': 4,
        }
    },
    '0x20B7:0x1610': {
        'id': 708,
        'name': 'NVIDIA A30-1-6CME',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x20B7:0x1589',  # NVIDIA A30-1-6C
        'DISABLE_ON': ['esx_aie_6_7', 'esx_aie_7_2', 'esx_aie_8_0', ],
        'OVERRIDES': {
            'max_instance': 1,
        }
    },
    '0x20B7:0x158A': {
        'id': 690,
        'name': 'NVIDIA A30-2-12C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x20B7:0x158F',  # NVIDIA A30-12C
        'OVERRIDES': {
            'gpuInstanceSize': 2,
            'max_instance': 2,
        }
    },
    '0x20B7:0x158B': {
        'id': 691,
        'name': 'NVIDIA A30-4-24C',
        'PGPU_SSID': '0x1532',
        'ATTR_LIKE': '0x20B7:0x1590',  # NVIDIA A30-24C
        'OVERRIDES': {
            'gpuInstanceSize': 4,
            'max_instance': 1,
            'multiVgpuSupported': 0,
            'nvlinkP2PSupported': 0,
        },
    },
    '0x25B6:0x159D': {
        'id': 709,
        'name': 'NVIDIA A16-1B',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14B6',  # NVIDIA A10-1B
    },
    '0x25B6:0x159E': {
        'id': 710,
        'name': 'NVIDIA A16-2B',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14B7',  # NVIDIA A10-2B
    },
    '0x25B6:0x159F': {
        'id': 711,
        'name': 'NVIDIA A16-1Q',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14B8',  # NVIDIA A10-1Q
    },
    '0x25B6:0x1600': {
        'id': 712,
        'name': 'NVIDIA A16-2Q',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14B9',  # NVIDIA A10-2Q
    },
    '0x25B6:0x1601': {
        'id': 713,
        'name': 'NVIDIA A16-4Q',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14BB',  # NVIDIA A10-4Q
    },
    '0x25B6:0x1602': {
        'id': 714,
        'name': 'NVIDIA A16-8Q',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14BD',  # NVIDIA A10-8Q
    },
    '0x25B6:0x1603': {
        'id': 715,
        'name': 'NVIDIA A16-16Q',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x1EB8:0x1310',  # GRID T4-16Q
    },
    '0x25B6:0x1604': {
        'id': 716,
        'name': 'NVIDIA A16-1A',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14C0',  # NVIDIA A10-1A
    },
    '0x25B6:0x1605': {
        'id': 717,
        'name': 'NVIDIA A16-2A',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14C1',  # NVIDIA A10-2A
    },
    '0x25B6:0x1606': {
        'id': 718,
        'name': 'NVIDIA A16-4A',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14C3',  # NVIDIA A10-4A
    },
    '0x25B6:0x1607': {
        'id': 719,
        'name': 'NVIDIA A16-8A',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14C5',  # NVIDIA A10-8A
    },
    '0x25B6:0x1608': {
        'id': 720,
        'name': 'NVIDIA A16-16A',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x1EB8:0x1315',  # GRID T4-16A
    },
    '0x25B6:0x1609': {
        'id': 721,
        'name': 'NVIDIA A16-4C',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14D0',  # NVIDIA A10-4C
    },
    '0x25B6:0x160A': {
        'id': 722,
        'name': 'NVIDIA A16-8C',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x2236:0x14D2',  # NVIDIA A10-8C
    },
    '0x25B6:0x160B': {
        'id': 723,
        'name': 'NVIDIA A16-16C',
        'PGPU_SSID': '0x14A9',
        'ATTR_LIKE': '0x1EB8:0x1375',  # GRID T4-16C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1
    },
    '0x25B6:0x1646': {
        'id': 742,
        'name': 'NVIDIA A2-1B',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14B6',  # NVIDIA A10-1B
    },
    '0x25B6:0x1647': {
        'id': 743,
        'name': 'NVIDIA A2-2B',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14B7',  # NVIDIA A10-2B
    },
    '0x25B6:0x1648': {
        'id': 744,
        'name': 'NVIDIA A2-1Q',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14B8',  # NVIDIA A10-1Q
    },
    '0x25B6:0x1649': {
        'id': 745,
        'name': 'NVIDIA A2-2Q',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14B9',  # NVIDIA A10-2Q
    },
    '0x25B6:0x164A': {
        'id': 746,
        'name': 'NVIDIA A2-4Q',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14BB',  # NVIDIA A10-4Q
    },
    '0x25B6:0x164B': {
        'id': 747,
        'name': 'NVIDIA A2-8Q',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14BD',  # NVIDIA A10-8Q
    },
    '0x25B6:0x164C': {
        'id': 748,
        'name': 'NVIDIA A2-16Q',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x1EB8:0x1310',  # GRID T4-16Q
    },
    '0x25B6:0x164D': {
        'id': 749,
        'name': 'NVIDIA A2-1A',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14C0',  # NVIDIA A10-1A
    },
    '0x25B6:0x164E': {
        'id': 750,
        'name': 'NVIDIA A2-2A',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14C1',  # NVIDIA A10-2A
    },
    '0x25B6:0x164F': {
        'id': 751,
        'name': 'NVIDIA A2-4A',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14C3',  # NVIDIA A10-4A
    },
    '0x25B6:0x1650': {
        'id': 752,
        'name': 'NVIDIA A2-8A',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14C5',  # NVIDIA A10-8A
    },
    '0x25B6:0x1651': {
        'id': 753,
        'name': 'NVIDIA A2-16A',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x1EB8:0x1315',  # GRID T4-16A
    },
    '0x25B6:0x1655': {
        'id': 754,
        'name': 'NVIDIA A2-4C',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14D0',  # NVIDIA A10-4C
    },
    '0x25B6:0x1656': {
        'id': 755,
        'name': 'NVIDIA A2-8C',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x2236:0x14D2',  # NVIDIA A10-8C
    },
    '0x25B6:0x1657': {
        'id': 756,
        'name': 'NVIDIA A2-16C',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x25B6:0x160B',  # GRID A16-16C
        'gpuDirectSupported': 1
    },
    '0x25B6:0x1652': {
        'id': 757,
        'name': 'NVIDIA A2-4',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x1EB8:0x1367',  # GRID RTX T4-4
    },
    '0x25B6:0x1653': {
        'id': 758,
        'name': 'NVIDIA A2-8',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x1EB8:0x1368',  # GRID RTX T4-8
    },
    '0x25B6:0x1654': {
        'id': 759,
        'name': 'NVIDIA A2-16',
        'PGPU_SSID': '0x157E',
        'ATTR_LIKE': '0x1E37:0x136C',  # GRID RTX T10-16
    },
    '0x2236:0x167E': {
        'id': 787,
        'name': 'NVIDIA A10-2',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '2G',
        'gpuDirectSupported': 1,
    },
    '0x2236:0x167F': {
        'id': 788,
        'name': 'NVIDIA A10-3',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '3G',
        'gpuDirectSupported': 1,
    },
    '0x2236:0x1680': {
        'id': 789,
        'name': 'NVIDIA A10-4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '4G',
        'gpuDirectSupported': 1,
    },
    '0x2237:0x155B': {
        'id': 790,
        'name': 'NVIDIA A10G-2',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '2G',
        'gpuDirectSupported': 1,
    },
    '0x2237:0x155C': {
        'id': 791,
        'name': 'NVIDIA A10G-3',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '3G',
        'gpuDirectSupported': 1,
    },
    '0x2237:0x155D': {
        'id': 792,
        'name': 'NVIDIA A10G-4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '4G',
        'gpuDirectSupported': 1,
    },
    '0x2235:0x1684': {
        'id': 793,
        'name': 'NVIDIA A40-2',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '2G',
        'gpuDirectSupported': 1,
    },
    '0x2235:0x1685': {
        'id': 794,
        'name': 'NVIDIA A40-3',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '3G',
        'gpuDirectSupported': 1,
    },
    '0x2235:0x1686': {
        'id': 795,
        'name': 'NVIDIA A40-4',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '4G',
        'gpuDirectSupported': 1,
    },
    '0x2235:0x1687': {
        'id': 796,
        'name': 'NVIDIA A40-6',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '6G',
        'gpuDirectSupported': 1,
    },
    '0x2235:0x1688': {
        'id': 797,
        'name': 'NVIDIA A40-8',
        'PGPU_SSID': 0,
        'ATTR_LIKE': 'GAMING_NGN_ATTRIBUTES',
        'FB_LIKE': '8G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16A3': {
        'id': 798,
        'name': 'NVIDIA A10M-1B',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11E7',  # P40-1B
    },
    '0x2238:0x16A4': {
        'id': 799,
        'name': 'NVIDIA A10M-2B',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x13F2:0x117D',  # M60-2B
    },
    '0x2238:0x16A5': {
        'id': 800,
        'name': 'NVIDIA A10M-1Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11E8',  # P40-1Q
    },
    '0x2238:0x16A6': {
        'id': 801,
        'name': 'NVIDIA A10M-2Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11E9',  # P40-2Q
    },
    '0x2238:0x16A7': {
        'id': 802,
        'name': 'NVIDIA A10M-4Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11EB',  # P40-4Q
    },
    '0x2238:0x16A8': {
        'id': 803,
        'name': 'NVIDIA A10M-5Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '5G',
    },
    '0x2238:0x16A9': {
        'id': 804,
        'name': 'NVIDIA A10M-10Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '10G',
    },
    '0x2238:0x16AA': {
        'id': 805,
        'name': 'NVIDIA A10M-20Q',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'QVDWS_ATTRIBUTES',
        'FB_LIKE': '20G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
        },
    },
    '0x2238:0x16AB': {
        'id': 806,
        'name': 'NVIDIA A10M-1A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11F0',  # P40-1A
    },
    '0x2238:0x16AC': {
        'id': 807,
        'name': 'NVIDIA A10M-2A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x13F2:0x11AF',  # M60-2A
    },
    '0x2238:0x16AD': {
        'id': 808,
        'name': 'NVIDIA A10M-4A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x11F3',  # P40-4A
    },
    '0x2238:0x16AE': {
        'id': 809,
        'name': 'NVIDIA A10M-5A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '5G',
    },
    '0x2238:0x16AF': {
        'id': 810,
        'name': 'NVIDIA A10M-10A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '10G',
    },
    '0x2238:0x16B0': {
        'id': 811,
        'name': 'NVIDIA A10M-20A',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'VAPPS_ATTRIBUTES',
        'FB_LIKE': '20G',
    },
    '0x2238:0x16B1': {
        'id': 812,
        'name': 'NVIDIA A10M-2',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '2G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B2': {
        'id': 813,
        'name': 'NVIDIA A10M-4',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '4G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B3': {
        'id': 814,
        'name': 'NVIDIA A10M-5',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '5G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B4': {
        'id': 815,
        'name': 'NVIDIA A10M-10',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '10G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B5': {
        'id': 816,
        'name': 'NVIDIA A10M-20',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'GAMING_ATTRIBUTES',
        'FB_LIKE': '20G',
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B6': {
        'id': 817,
        'name': 'NVIDIA A10M-4C',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': '0x1B38:0x1381',  # P40-4C
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B7': {
        'id': 818,
        'name': 'NVIDIA A10M-5C',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '5G',
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B8': {
        'id': 819,
        'name': 'NVIDIA A10M-10C',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '10G',
        'OVERRIDES': {
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    },
    '0x2238:0x16B9': {
        'id': 820,
        'name': 'NVIDIA A10M-20C',
        'PGPU_SSID': '0x1677',
        'ATTR_LIKE': 'COMPUTE_ATTRIBUTES',
        'FB_LIKE': '20G',
        'OVERRIDES': {
            'multiVgpuSupported': 1,
            'bar1Length': '0x800',
        },
        'gpuDirectSupported': 1,
    }
}