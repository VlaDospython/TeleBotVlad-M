import os
import telebot

# My name is VLAD_M_TELEGRAM_BOT_1_TOKEN
token = os.environ['VLAD_M_TELEGRAM_BOT_1_TOKEN']
bot = telebot.TeleBot(token, parse_mode='MarkdownV2')

msg = r"""
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
lst = [1, 2, 3]
for x in lst:
    print(x)
```
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity
>Expandable block quotation continued
>Hidden by default part of the expandable block quotation started
>Expandable block quotation continued
>The last line of the expandable block quotation with the expandability mark||"""


@bot.message_handler(commands=['msg'])
def command_bold(message):
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['bold'])
def command_bold(message):
    text = f"*{str(message.text)[1:]}*"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['italic'])
def command_bold(message):
    text = f"_{str(message.text)[1:]}_**"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['underline'])
def command_italic(message):
    text = f"__{str(message.text)[1:]}__"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['strikethrough'])
def command_italic(message):
    text = f"~{str(message.text)[1:]}~"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['spoiler'])
def command_italic(message):
    text = f"||{str(message.text)[1:]}||"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['url'])
def command_italic(message):
    text = f"[{str(message.text)[1:]}](https://docs.google.com/document/d/1_G_VpmlDKR3zLSsQ-J7-Gchh-kXKyruHsMEVwdlAC0E/edit#heading=h.gx131h45q22x)"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['sticker'])
def command_italic(message):
    text = f"{str(message.text)[1:]} 👍"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['fixed_code'])
def command_italic(message):
    text = f"`{str(message.text)[1:]}`"
    bot.send_message(message.chat.id, text)


code_block = '''
number = int(input("Enter a number: "))
print("Numbers from 0 to " + str(number) + ":")
for i in range(number):
    print(str(i) + ":")
'''


@bot.message_handler(commands=['code_block'])
def command_italic(message):
    text = f"```{str(message.text)[1:]}```"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['python_block'])
def command_italic(message):
    text = f"```python{code_block}```"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['block_quotation'])
def command_italic(message):
    text = r"""
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>Block quotation continued
>Block quotation continued
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation"""
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['block_quotation2'])
def command_italic(message):
    text = r"""
    **\>The expandable block quotation started right after the previous block quotation
\>It is separated from the previous block quotation by an empty bold entity
\>Expandable block quotation continued
\>Hidden by default part of the expandable block quotation started
\>Expandable block quotation continued
\>The last line of the expandable block quotation with the expandability mark"""
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.infinity_polling()


# start - Почати спілкування з Мухой повторюхой
# stop - Закінчити спілкування з Мухой повторюхой
# msg - Виводить весь форматований текст
# bold - Жирний текст
# italic - Похилений текст
# underline - Підкреслений текст
# strikethrough - Закреслений текст
# spoiler - Текст позначений як спойлер
# url - Посилання на документ
# sticker - Лайк
# fixed_code - Текст виглядає як змінений код
# code_block - Блок коду
# python_block - Блок коду на пайтон
# block_quotation - Цитата
# block_quotation2 - Цитата яку можна писати після попередньої цитати