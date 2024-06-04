from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
import os
from kbds import reply
import datetime
from table.read import title, sum_men


user_private_router = Router()



@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Приветстую! \n'
                         'Я твой помощник в работе по охране труда, в компании ООО "Модтфил". \n'
                         'Пока что мой функцинал ограничен, но я активно развиваюсь.\n'
                         'Мой создатель: Бычков Андрей',
                         reply_markup=reply.start_kb3.as_markup(
                            resize_keyboard=True,
                            input_field_placeholder='Выбирете команду'))
    await message.answer('Чем могу помочь?')


file = ['', '']
file_1 = ''


@user_private_router.message(F.text.lower().contains("докум"))
@user_private_router.message(Command("docx"))
async def docx(message: types.Message):
    await message.answer_document(document=types.FSInputFile(path=file[0]))
    await message.answer_document(document=types.FSInputFile(path=file[1]))

@user_private_router.message(F.text.lower().contains("наряд"))
@user_private_router.message(Command("docx_2"))
async def docx_1(message: types.Message):
    await message.answer_document(document=types.FSInputFile(path=file_1))

@user_private_router.message(F.text.lower() == "о проекте")
@user_private_router.message(Command("proekt"))
async def about_cmd(message: types.Message):
    await message.answer('Национальный космический центр (НКЦ) — строящийся в Москве, на свободной территории ГКНПЦ имени Хруничева в Филях, аэрокосмический кластер.\n'
                         'В НКЦ под одной крышей планируется объединить 18 из 30 московских КБ и предприятий ракетно-космической отрасли Москвы — в сумме, около 12 тысяч сотрудников.\n'
                         'Итого, вместе с 8 тысячами сотрудников Центра им. Хруничева, в кластере будут работать около 20 тысяч человек. Он станет филиалом Особой экономической зоны Технополис «Москва»')



@user_private_router.message(F.text.lower().contains('работник'))
@user_private_router.message(Command("title"))
async def payment_cmd(message: types.Message):
    await message.answer(f'Всего сотрудников: {sum_men} \n {title}')


@user_private_router.message((F.text.lower().contains("other")) | (F.text.lower() == "прочее"))
@user_private_router.message(Command("other"))
async def menu_cmd(message: types.Message):
    await message.answer('Прочее')


t = datetime.datetime.now().time().strftime('%H:%M')
@user_private_router.message(F.text.lower().contains("врем"))
async def time(message: types.Message):
    await message.answer(f'На данный момент время по Москве составляет: {t}')


@user_private_router.message(F.text.lower().contains("анекдот"))
async def reminder(message: types.Message):
    await message.answer('Если хочешь посмеяться, то посмотри на свою зарплату')

@user_private_router.message(F.text.lower().contains('Высот'))
async def p_1(message: types.Message):
    await message.answer(f'Данные по обучению для работы на высоте: {inf_1}')

@user_private_router.message(F.text.lower().contains('сотрудник'))
@user_private_router.message(Command("title"))
async def payment_cmd(message: types.Message):
    await message.answer(f'Всего сотрудников: {sum_men} \n {title}')

@user_private_router.message()
async def wer(message: types.Message):
    await message.answer('Не могу распознать команду! \n'
                         'Пожалуйста, воспользуйтесь командами на вашем меню.')



