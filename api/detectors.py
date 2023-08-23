def detect_lang(func):
    def method(self, request, *args, **kwargs):
        lang = request.COOKIES.get('lang', 'en').lower()
        return func(self, request, lang, *args, **kwargs)
    return method