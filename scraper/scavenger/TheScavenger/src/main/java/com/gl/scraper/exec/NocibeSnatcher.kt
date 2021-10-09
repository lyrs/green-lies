package com.gl.scraper.exec

import com.gl.scraper.candleblower.IAdaptorMaster
import com.gl.scraper.dto.RawProductInfo

class NocibeSnatcher : IAdaptorMaster{
    override fun getFromSephora(url: String): RawProductInfo {
        return RawProductInfo()
    }

    override fun getFromNocibe(url: String): RawProductInfo {
        return RawProductInfo()    }

    override fun getFromMarionnaud(url: String): RawProductInfo {
        return RawProductInfo()    }
}