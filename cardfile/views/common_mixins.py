

class NavMixin:
    navs = {'cardfile:base': 'Базовая страница',
            'cardfile:composer': 'Композиторы',
            'cardfile:genre': 'Жанры',
            'cardfile:author_of_text': 'Авторы текста',
            'cardfile:performer': 'Исполнители',
            'cardfile:artwork': 'Произведения',
            'cardfile:performance': 'Исполнения',
            'cardfile:record': 'Пластинки'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['nav_names'] = self.get_nav_names()
        return context

    def get_nav_names(self):
        return self.navs


class FiltersMixin:

    def get_filters(self):
        return None

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['filter'] = self.get_filters()
        return context



