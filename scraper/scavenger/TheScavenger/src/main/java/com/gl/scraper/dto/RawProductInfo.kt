package com.gl.scraper.dto

class RawProductInfo(private var name:String = " ", private var ingredients: String = "", private var claims: String = "") {
    fun getName() : String {
        return name
    }
    fun getIngredients() : String {
        return ingredients
    }
    fun getClaims() : String {
        return claims
    }
}