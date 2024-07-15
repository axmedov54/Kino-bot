import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from config import token
from buttons import kodlarni_qidirish, kanalga_otish, admin_first, ha_or_yoq, finish_setup
from states import Kino, Admin  
from fetch_db import fetch_data
from insert_db import insert_data

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command('start'))
async def StartCommand(message: types.Message, state: FSMContext):
    await state.set_state(Kino.code)
    await message.answer(text=f"Salom{message.from_user.full_name}Bizda xozircha faqar bitta serial bor",reply_markup=kodlarni_qidirish
    )

@dp.message(Command('search'))
async def StartCommand(message: types.Message, state: FSMContext):
    await state.set_state(Kino.code)
    await message.answer(text=f"Salom {message.from_user.full_name}bizda bitta serial bor", reply_markup=kodlarni_qidirish
    )

@dp.message(Command('admin'))
async def AdminCommand(message: types.Message, state: FSMContext):
    await message.answer("Hurmatli admin, 'database'ga yangi kino qo'shmoqchimisiz?", reply_markup=admin_first)

@dp.message(F.text == 'Ha')
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    await state.set_state(Admin.nomi)
    await message.answer('Kino nomini kiriting!')

@dp.message(F.text == "Yo'q, keyinroq")
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    await message.answer("Buyruq bekor qilindi.\nYangi kino yuklash uchun /admin buyrug'idan foydalaning\nKinolarni qidirish uchun esa /search")
    await state.clear()
    


@dp.message(Admin.video_url)
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    kino_video_url = message.text
    await state.update_data(
        {'video_url': kino_video_url}
    )
    data = await state.get_data()
    await message.answer_video(
                video=data['video_url'], 
                caption=f"\n🎦 Nomi: {data['nomi']}\n🎥 Kanal:t.me/+A_YFxv75Il85NWYy", 
            )
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ha_or_yoq)
    await state.set_state(Admin.finish)

@dp.message(Admin.finish)
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    finish_check = message.text
    data = await state.get_data()
    if finish_check == "Ha, to'gri!":
        insert_data(name=data['nomi'], video_url=data['video_url'])
        await message.answer("Yangi kino muvaffaqiyatli saqlandi!", reply_markup=finish_setup)
        await state.set_state(Admin.leave)
    elif finish_check == "Yo'q, xatolik bor!":
        await message.answer("Ma'lumot yuklanmadi.\nYangi kino yuklash uchun /admin buyrug'idan foydalaning\nKinolarni qidirish uchun esa /search")
        await state.clear()

@dp.message(Admin.leave)
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    user_choice = message.text
    if user_choice == "Yana qo'shish":
        await message.answer('Kino nomini kiriting!')
        await state.set_state(Admin.nomi)
    elif user_choice == "Tugatish":
        await message.answer("Yangi kino yuklash uchun /admin buyrug'idan foydalaning\nKinolarni qidirish uchun esa /search")
        await state.clear()


@dp.message(Kino.code)
async def TranslateLangCommand(message: types.Message, state: FSMContext):
    code = message.text
    data = fetch_data()
    for i in data:
        if int(code) == int(i[0]):
            await message.answer_video(
                video=i[2], 
                caption=f"\n🎦 Nomi: {i[1]}\n🎥 Kanal:t.me/+A_YFxv75Il85NWYy {i[3]}", 
                reply_markup=kanalga_otish
            )
            break
    await state.set_state(Kino.code)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())