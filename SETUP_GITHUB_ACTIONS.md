# Настройка GitHub Actions для Allure отчетов

## Пошаговая инструкция

### 1. Создание репозитория на GitHub

1. Создайте новый репозиторий на GitHub
2. Загрузите ваш код в репозиторий:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with Allure setup"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### 2. Настройка GitHub Pages

1. Перейдите в **Settings** вашего репозитория
2. Найдите раздел **Pages** в левом меню
3. В разделе **Source** выберите **GitHub Actions**
4. Сохраните изменения

### 3. Автоматические переменные

GitHub автоматически предоставляет следующие переменные:

- `${{ secrets.GITHUB_TOKEN }}` - встроенный токен (не требует настройки)
- `${{ github.repository_owner }}` - владелец репозитория
- `${{ github.event.repository.name }}` - название репозитория

### 4. Проверка workflow

После настройки:

1. Сделайте push в ветку `main`
2. Перейдите во вкладку **Actions** в вашем репозитории
3. Убедитесь, что workflow запустился
4. После успешного выполнения откройте **Pages** в настройках
5. Нажмите на ссылку для просмотра сайта

### 5. Структура файлов

Убедитесь, что у вас есть следующие файлы:
- `.github/workflows/test-and-deploy.yml`
- `requirements.txt`
- `pytest.ini`
- `conftest.py`
- `allure.properties`

### 6. Возможные проблемы

**Проблема**: Workflow не запускается
**Решение**: Убедитесь, что файл находится в `.github/workflows/` и имеет расширение `.yml`

**Проблема**: GitHub Pages не работает
**Решение**: 
1. Проверьте, что в Settings → Pages выбран "GitHub Actions"
2. Убедитесь, что у workflow есть права `pages: write`

**Проблема**: Тесты не запускаются
**Решение**: Проверьте зависимости в `requirements.txt` и структуру тестов

### 7. Просмотр отчетов

После успешного деплоя отчеты будут доступны по адресу:
`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

## Дополнительные настройки

### Настройка уведомлений

Для получения уведомлений о результатах тестов добавьте в workflow:

```yaml
- name: Notify on failure
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: failure
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

### Настройка расписания

Для запуска тестов по расписанию добавьте в `on:`:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Каждый день в 2:00 UTC
```

### Настройка переменных окружения

Если нужны дополнительные переменные, добавьте их в Settings → Secrets and variables → Actions:

1. **Repository secrets** - для чувствительных данных (API ключи, токены)
2. **Repository variables** - для обычных переменных (URLs, пути)
