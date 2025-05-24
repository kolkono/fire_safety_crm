import { test, expect } from '@playwright/test';

test('Проверка загрузки списка клиентов', async ({ page }) => {
  await page.goto('http://localhost:8000/clients/');

  // Проверяем, что заголовок страницы есть и правильный
  await expect(page.locator('h1')).toHaveText('Клиенты');

  // Проверяем наличие кнопки "Добавить клиента"
  await expect(page.locator('a', { hasText: 'Добавить клиента' })).toBeVisible();
});
