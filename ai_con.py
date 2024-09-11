from openai import OpenAI

# Инициализация клиента
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def chat_with_gpt():
    messages = []  # Список сообщений для общения с моделью

    print("Вы можете начать общение с GPT-3.5. Для выхода введите 'выход'.")

    while True:
        user_input = input("Вы (введите 'выход' для завершения): ")

        if user_input.lower() == 'выход':
            print("Завершение общения.")
            break

        # Добавляем сообщение пользователя в список
        messages.append({"role": "user", "content": user_input})

        # Отправляем запрос к модели
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", messages=messages
        )

        # Получаем и отображаем ответ модели
        # bot_response = response['choices'][0]['message']['content']
        bot_response= response.choices[0].message.content
        print("GPT-3.5:", bot_response)

        # Добавляем ответ модели в список
        messages.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    chat_with_gpt()