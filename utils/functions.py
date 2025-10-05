import allure

def attach_regress(response):
    """Прикрепляет данные запроса к Allure-отчету."""
    request = response.request

    attachments = {
        "Метод Запроса": request.method,
        "URL Запроса": request.url,
    }

    for name, value in attachments.items():
        allure.attach(
            str(value),
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )