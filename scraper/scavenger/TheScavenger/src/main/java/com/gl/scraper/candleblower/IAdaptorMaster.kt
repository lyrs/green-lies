package com.gl.scraper.candleblower

import com.gl.scraper.dto.RawProductInfo

interface IAdaptorMaster {
    fun getFromSephora(url: String) : RawProductInfo
    fun getFromNocibe(url: String) : RawProductInfo
    fun getFromMarionnaud(url: String) : RawProductInfo
}