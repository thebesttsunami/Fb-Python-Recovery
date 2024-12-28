#!/user/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Buat objek webdriver
driver = webdriver.Chrome()

Buka halaman Facebook
driver.get("(link unavailable)")

Masukkan email dan password
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)
email_input.send_keys("email_anda")

password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys("password_anda")

Klik tombol Masuk
masuk_button = driver.find_element(By.NAME, "login")
masuk_button.click()

Klik tombol Lupa Akun
lupa_akun_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/recover/initiate/']"))
)
lupa_akun_button.click()

Isi formulir pemulihan
nama_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "identifier"))
)
nama_input.send_keys("nama_anda")

Klik tombol Lanjutkan
lanjutkan_button = driver.find_element(By.NAME, "did_submit")
lanjutkan_button.click()

print("Akun sedang dipulihkan...")
