from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
import os

blacklist = ['drive.google.com', 'tor.checker.in']
HOME = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Format - PDF', callback_data='format')],
            [InlineKeyboardButton(text='Page - Full', callback_data="page")],
            # [InlineKeyboardButton(text='Landscape', callback_data="orientation")],
            [InlineKeyboardButton(text='show additional options ˅', callback_data="options")],
            [InlineKeyboardButton(text='▫️ start render ▫️', callback_data="render")],
            [InlineKeyboardButton(text='cancel', callback_data="cancel")]
                            ])
format_for_logging = "Request from {name} aka @{user}\n\nQuery : {link}\n\nSettings Used : \n {settings}"


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Please Send Any Link",
        reply_to_message_id=message.message_id
    )


@Client.on_message(Filters.command(["feedback"]))
async def feedback(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"for suggetions and feedbacks contact @WhatsAGroup",
        reply_to_message_id=message.message_id
    )


@Client.on_message(Filters.command(["about"]))
async def about(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text='This bot is featured by @WhatsABot ',
        disable_web_page_preview=True
    )


@Client.on_message(Filters.command(["notworking"]))
async def notworking(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Make sure Your Request has http or https prefix",
        reply_to_message_id=message.message_id
    )


@Client.on_message(Filters.command(["delete"]) & Filters.private)
async def deleter_(client, message):
    try:
        sudo_user = int(os.environ["SUDO_USER"])
    except Exception:
        return False
    if message.from_user.id == sudo_user:
        random_message = await message.reply_text('Processing')
        if os.path.isdir('./FILES/'):
            with open('walk.txt', 'w') as writer:
                for root, dirs, files in os.walk('./FILES/', topdown=False):
                    writer.write(str(root)+'\n\n'+str(dirs)+'\n\n'+str(files))
            if os.path.isfile('walk.txt'):
                await client.send_document(
                    document='walk.txt',
                    chat_id=message.chat.id
                )
                await random_message.delete()
                os.remove('walk.txt')
                await message.reply_text(
                    text='Do you want to delete?',
                    reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text='Yes', callback_data='deleteyes')],
                    [InlineKeyboardButton(text='No', callback_data='deleteno')],
                    ])
                    )
    else:
        return


@Client.on_message(Filters.command(["report"]) & Filters.private)
async def delete(client, message):
    try:
        sudo_user = int(os.environ["SUDO_USER"])
    except Exception:
        return False
    if message.reply_to_message is not None:
        if message.reply_to_message.from_user.is_self:
            message_to_send = message.reply_to_message.text
            await client.send_message(
                sudo_user,
                message_to_send
            )
            await message.reply_text("report successfully send")
        else:
            await message.reply_text("don't spam please")
    else:
        await message.reply_text("just tag the error message and use /report command")
