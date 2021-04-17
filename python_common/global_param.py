from file_and_system.config_utils import ConfigUtils
import os


class GlobalParam:
    project_path = os.path.dirname(os.getcwd())
    conf_path = ''.join((project_path + r'\test file\cf.properties'))
    # print(sys.path[0])
    # print(os.path.dirname(os.getcwd()))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(sys.path[1])
    # conf_path = r'D:\ivanovsky\IdeaProjects\cowabunga-potato\test file\cf.properties'
    section_test_path = 'test_path'
    section_opencv_utils = 'opencv_utils'
    section_machine_learning = 'machine_learning'
    section_appium = 'appium'
    section_selenium = 'selenium'
    section_databases = 'databases'
    section_test_reports = 'testReports'

    # test_path section
    @staticmethod
    def get_test_image_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_test_path, 'test_image_path')[2]))

    @staticmethod
    def get_test_video_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_test_path, 'test_video_path')[2]))

    @staticmethod
    def get_test_file_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_test_path, 'test_file_path')[2]))

    # opencv_utils section
    @staticmethod
    def get_system_font_path():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'system_font_path')[2]

    @staticmethod
    def get_tesseract_path():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'tesseract_path')[2]

    @staticmethod
    def get_image_input():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'image_input')[2]))

    @staticmethod
    def get_image_output():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'image_output')[2]))

    @staticmethod
    def get_character_output():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'character_output')[2]))

    @staticmethod
    def get_sentence_output():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'sentence_output')[2]))

    @staticmethod
    def get_video_input():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'video_input')[2]))

    @staticmethod
    def get_video_output():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'video_output')[2]))

    @staticmethod
    def get_face_detect_face_xml():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'face_detect_face_xml')[
                            2]))

    @staticmethod
    def get_face_detect_eyes_xml():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_opencv_utils, 'face_detect_eyes_xml')[
                            2]))

    # appium section
    @staticmethod
    def get_aapt_path():
        return ''.join(
            (GlobalParam.project_path, ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_appium, 'aapt_path')[2]))

    @staticmethod
    def get_android_apk_list():
        return ''.join(
            (GlobalParam.project_path, ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_appium, 'android_apk_list')[2]))

    @staticmethod
    def get_appium_screenshot_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_appium, 'appium_screenshot_path')[2]))

    @staticmethod
    def get_appium_screenrecord_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_appium, 'appium_screenrecord_path')[2]))

    @staticmethod
    def get_qr_code_image_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_appium, 'qr_code_image_path')[2]))

    # machine learning section
    @staticmethod
    def get_ml_ch2_housing_data():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_machine_learning,
                                                   'ml_ch2_housing_data')[2]))

    @staticmethod
    def get_ml_ch2_housing_image():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_machine_learning,
                                                   'ml_ch2_housing_image')[2]))

    @staticmethod
    def get_ml_ch3_sklearn_data_home():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_machine_learning,
                                                   'ml_ch3_sklearn_data_home')[2]))

    @staticmethod
    def get_ml_numpy_array_save_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_machine_learning,
                                                   'ml_numpy_array_save_path')[2]))

    @staticmethod
    def get_ml_matplotlib_figure_save_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_machine_learning,
                                                   'ml_matplotlib_figure_save_path')[2]))

    # selenium section
    @staticmethod
    def get_chrome_driver_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_selenium, 'chrome_driver_path')[2]))

    @staticmethod
    def get_ie_driver_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_selenium, 'ie_driver_path')[2]))

    @staticmethod
    def get_edge_driver_path():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_selenium, 'edge_driver_path')[2]))

    @staticmethod
    def get_chromium_path():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_selenium, 'chromium_path')[2]

    # databases section
    @staticmethod
    def get_mariadb_url():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'mariadb_url')[2]

    @staticmethod
    def get_mariadb_user():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'mariadb_user')[2]

    @staticmethod
    def get_mariadb_password():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'mariadb_password')[2]

    @staticmethod
    def get_pgsql_url():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'pgsql_url')[2]

    @staticmethod
    def get_pgsql_user():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'pgsql_user')[2]

    @staticmethod
    def get_pgsql_password():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'pgsql_password')[2]

    @staticmethod
    def get_excel_datasets():
        return ''.join((GlobalParam.project_path,
                        ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_databases, 'excel_datasets')[2]))

    @staticmethod
    def get_csv_datasets():
        return ''.join(
            (GlobalParam.project_path, ConfigUtils.read_conf_file(GlobalParam.conf_path,
                                                                  GlobalParam.section_databases, 'csv_datasets')[2]))

    # test_reports section
    @staticmethod
    def get_unittest_reports():
        return ConfigUtils.read_conf_file(GlobalParam.conf_path, GlobalParam.section_test_reports, 'unittest_reports')[2]