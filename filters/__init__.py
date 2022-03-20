from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . guruhlar_bilan_ishlash import Gurux
from . kanallar_bilan_ishlash import Konal
from . userlar_bilan_ishlash import Shaxsiy

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
   dp.filters_factory.bind(Gurux)
   dp.filters_factory.bind(Shaxsiy)
   dp.filters_factory.bind(Konal)
