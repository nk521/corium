#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apk import APK


def test():
    apk_path = "../test.apk"
    #apk_path = "/home/sym/Downloads/share/11/davm/app/com.tmob.AveaOIM.apk"
    apkf = APK(apk_path)
    print(f"{apkf.cert_text=}")
    print(f"{apkf.file_md5=}")
    print(f"{apkf.cert_md5=}")
    print(f"{apkf.file_size=}")
    print(f"{apkf.androidversion=}")
    print(f"{apkf.package=}")
    print(f"{apkf.get_android_manifest_xml()=}")
    print(f"{apkf.get_android_manifest_axml()=}")
    print(f"{apkf.is_valid_APK()=}")
    print(f"{apkf.get_filename()=}")
    print(f"{apkf.get_package()=}")
    print(f"{apkf.get_androidversion_code()=}")
    print(f"{apkf.get_androidversion_name()=}")
    print(f"{apkf.get_max_sdk_version()=}")
    print(f"{apkf.get_min_sdk_version()=}")
    print(f"{apkf.get_target_sdk_version()=}")
    print(f"{apkf.get_libraries()=}")
    print(f"{apkf.get_files()=}")
    # pip install python-magic
    print(apkf.get_files_types())
    print(apkf.get_dex())
    print(apkf.get_main_activity())
    print(apkf.get_activities())
    print(apkf.get_services())
    print(apkf.get_receivers())
    print(apkf.get_providers())
    print(apkf.get_permissions())
    print(apkf.show())
    # apkf.parse_icon(icon_path='/tmp')

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