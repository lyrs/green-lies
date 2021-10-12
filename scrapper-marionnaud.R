library(rvest)
library(dplyr)
library(stringr)


extract_data <- function(url) {
  simple <- read_html(url)
  temp <- simple %>%
    html_nodes(".productInformationSection") %>%
    html_nodes(".row")
  data <- setNames(temp %>% html_node("p") %>% html_text(), temp %>%
    html_node("h3") %>%
    html_text(trim = TRUE))
  data["BRRAND_NAME"] <- simple %>%
    html_nodes('.productBrandName') %>%
    html_text(trim = TRUE)
  data["RANGE"] <- simple %>%
    html_nodes('.producRangeName') %>%
    html_text(trim = TRUE)
  data["NAME"] <- simple %>%
    html_nodes('.productName') %>%
    html_text(trim = TRUE)
  data["ID"] <- str_replace(simple %>%
                              html_nodes('.product-code') %>%
                              html_text(trim = TRUE), "Ref: ", "")
  data
}

extract_product_link <- function(index) {

  url <- str_glue('https://www.marionnaud.fr/tous-les-produits?q=%3Arank-desc&page={index}&pageSize=100')

  prod <- read_html(url)

  temp <- prod %>%
    html_nodes(".product-listing ") %>%
    html_nodes(".productMainLink ") %>%
    html_node(".ProductInfoAnchor") %>%
    html_attr("href")

  temp <- lapply(temp,function (x){
    paste0("https://www.marionnaud.fr", x)
  })

temp
}

items <- array()

for (index in range(0, 77)) {
  items <-  append(items,extract_product_link(index))
}


all_data <- lapply(items,extract_data)
