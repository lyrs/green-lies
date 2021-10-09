package com.gl.scraper.dummy

import org.jsoup.Jsoup


class DummyRetriever {

}
fun main(args: Array<String>){
//    val url = "https://www.sephora.fr/p/sisleya-l-integral-anti-age---creme-contour-des-yeux-et-des-levres-P3083010.html"
    val url = "https://www.nocibe.fr/dior-miss-dior-eau-de-parfum-30-ml-s270773"
//    val url = "https://www.marionnaud.fr/soin-visage/hydratant-et-nourrissant/soin-de-jour/hydratation-creme-nourrissante-a-lhuile-dabricot-et-aloe-vera-herbal-essentials/p/102147492"
    val doc = Jsoup.connect(url).get()
    println(doc.toString())
}