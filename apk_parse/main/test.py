#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apk import APK
import pprint
pp = pprint.PrettyPrinter(indent=4)

def test():
    apk_path = "../test.apk"
    #apk_path = "/home/sym/Downloads/share/11/davm/app/com.tmob.AveaOIM.apk"
    apkf = APK(apk_path)
    
    print(f"{apkf.get_app_name()= }\n")
    print(f"{apkf.androidversion= }\n")
    print(f"{apkf.filename= }\n")
    print(f"{apkf.get_activities()= }\n")
    print(f"{apkf.get_androidversion_code()= }\n")
    print(f"{apkf.get_androidversion_name()= }\n")
    print(f"{apkf.get_declared_permissions()= }\n")
    print(f"{apkf.get_declared_permissions_details()= }\n")
    print(f"{apkf.get_details_permissions()= }\n")
    print(f"{apkf.get_effective_target_sdk_version()= }\n")
    print(f"{apkf.get_libraries()= }\n")
    print(f"{apkf.get_main_activities()= }\n")
    print(f"{apkf.get_main_activity()= }\n")
    print(f"{apkf.get_max_sdk_version()= }\n")
    print(f"{apkf.get_min_sdk_version()= }\n")
    print(f"{apkf.get_package()= }\n")
    print(f"{apkf.get_providers()= }\n")
    print(f"{apkf.get_receivers()= }\n")
    print(f"{apkf.get_requested_aosp_permissions()= }\n")
    print(f"{apkf.get_requested_aosp_permissions_details()= }\n")
    print(f"{apkf.get_requested_permissions()= }\n")
    print(f"{apkf.get_requested_third_party_permissions()= }\n")
    print(f"{apkf.get_services()= }\n")
    print(f"{apkf.get_uses_implied_permission_list()= }\n")
    print(f"{apkf.is_signed()= }\n")
    print(f"{apkf.is_valid_APK()= }\n")
    print(f"{apkf.is_wearable()= }\n")
    # print(f"{apkf.package= }\n")
    # print(f"{apkf.permissions= }\n")
    # print(f"{apkf.show= }\n")
    # print(f"{apkf.uses_permissions= }\n")
    # print(f"{apkf.valid_apk= }\n")



    # print(f"{apkf.is_signed_v1= }\n")
    # print(f"{apkf.is_signed_v2= }\n")
    # print(f"{apkf.is_signed_v3= }\n")
    # print(f"{apkf.is_tag_matched= }\n")

    ## Really long outputs
    # print(f"{apkf.files=}")
    # print(f"{apkf.get_raw()=}") # throws the entire ZIP
    # print(f"{apkf.get_certificates()=}")
    # print(f"{apkf.get_certificates_der_v2()=}")
    # print(f"{apkf.parse_signatures_or_digests=}")
    # print(f"{apkf.parse_v2_signing_block=}")
    # print(f"{apkf.get_signature()=}")
    # print(f"{apkf.get_signature_name()=}")
    # print(f"{apkf.get_signature_names()=}")
    # print(f"{apkf.get_signatures()=}")
    # print(f"{apkf.parse_v2_v3_signature=}")
    # print(f"{apkf.parse_v3_signing_block=}")
    # print(f"{apkf.read_uint32_le=}")
    # print(f"{apkf.permission_module=}")
    # print(f"{apkf.get_certificates_der_v3()=}")
    # print(f"{apkf.get_certificates_v1()=}")
    # print(f"{apkf.get_certificates_v2()=}")
    # print(f"{apkf.get_certificates_v3()=}")

if __name__ == "__main__":
    test()
    pass
    # a=set()
    # b=set()
    # a.add(1)
    # a.add(2)
    # print a
    # b.add(2)
    # b.add(3)
    # print b
    # print a.intersection(b)