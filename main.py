from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
#options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

categories = ["league-of-legends", "valorant", "teamfight-tactics", "arcane"]

base_url = "https://merch.riotgames.com/fr-fr/category/"

driver.get('https://merch.riotgames.com/fr-fr/shop-all')
try:
    cookie_ok_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.osano-cm-accept-all.osano-cm-buttons__button.osano-cm-button.osano-cm-button--type_accept")))
    cookie_ok_button.click()
except TimeoutException:
    print("Pas de cookie")

time.sleep(5)
all_products = []

for category in tqdm(categories, desc="Traitement des catégories"):
    url = f"{base_url}{category}/"
    driver.get(url)
    while True:
        try:
            #load_more_button = WebDriverWait(driver, 10).until(
            #EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button_button__52Aro.button_button--variant--primary__9pWMF.button_button--theme--default__QzKIY"))
            #)
            #load_more_button.click()
            
            # Attendre et cliquer sur un éventuel second bouton
            secondary_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/section/div/div/button"))
            )
            secondary_button.click()
        except Exception:
            print("Plus de bouton") 
            print("Changement de catégorie")
            break
    product_cards = driver.find_elements(By.CSS_SELECTOR, "article.product-card_product-card__LIKK8")

    for card in tqdm(product_cards, desc="Traitement des produits"):
        product_url = card.find_element(By.CSS_SELECTOR, "a.product-card_product-link__6pYsY").get_attribute("href")
        product_name = card.find_element(By.CSS_SELECTOR, "a.product-card_product-link__6pYsY").get_attribute("aria-label").replace("Voir ", "")
        product_price = card.find_element(By.CSS_SELECTOR, "span.text_text__84aqk.text-span.text-body.text_text--size--rg__GF7_L.add-to-cart-panel_panel-header__subheading__m_kc_").text
        try:
            limited_edition_elements = card.find_elements(By.CSS_SELECTOR, "span.tag_tag__ew8Dg.tag_tag--size--sm__EU94h")
            limited_edition = [element.text for element in limited_edition_elements]
        except Exception:
            limited_edition = None
        try:
            image_elements = card.find_elements(By.CSS_SELECTOR, "div.image_image__AxgoZ.product-card_image-item__RuQVM > img")
            product_images = [img.get_attribute("src") for img in image_elements]
        except Exception:
            product_image = None
        all_products.append({
            "name": product_name,
            "url": product_url,
            "price": product_price,
            "limited_edition": limited_edition,
            "category": category,
            "image": product_images
        })

        with open("products.json", "w") as file:
            json.dump(all_products, file, indent=4, ensure_ascii=False)

driver.quit()
