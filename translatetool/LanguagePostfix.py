from translatetool.ms.ms_language import *


class LanguagePostfix:
    english = "EN"
    chinese = "CN"
    korean = "KO"
    japanese = "JA"
    russian = "RU"
    thai = "TH"

    @staticmethod
    def get_language_postfix_list():
        postfix_list = [LanguagePostfix.english,
                        LanguagePostfix.chinese,
                        LanguagePostfix.japanese,
                        LanguagePostfix.korean,
                        LanguagePostfix.russian,
                        LanguagePostfix.thai]
        return postfix_list

    @staticmethod
    def get_ms_lan_list():
        ms_lan_list = [MSSupportLanguage.english,
                       MSSupportLanguage.simplified_chinese,
                       MSSupportLanguage.japanese,
                       MSSupportLanguage.korean,
                       MSSupportLanguage.russian,
                       MSSupportLanguage.thai]
        return ms_lan_list

    @staticmethod
    def get_lan_code_by_postfix(postfix: str):
        postfix_list = LanguagePostfix.get_language_postfix_list()
        ms_lan_list = LanguagePostfix.get_ms_lan_list()
        return ms_lan_list[postfix_list.index(postfix)]

    @staticmethod
    def get_post_fix_by_ms_lan_code(lan_code: str):
        postfix_list = LanguagePostfix.get_language_postfix_list()
        ms_lan_list = LanguagePostfix.get_ms_lan_list()
        return postfix_list[ms_lan_list.index(lan_code)]

