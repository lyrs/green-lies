package com.gl.scraper.exec

import com.gl.scraper.candleblower.IAdaptorMaster
import com.gl.scraper.dto.RawProductInfo

class SephoraSnatcher : IAdaptorMaster {
    override fun getFromSephora(url: String): RawProductInfo {
        TODO("Not yet implemented")

    }

    override fun getFromNocibe(url: String): RawProductInfo {
        //Sephora doesn't like Nocibé
        return RawProductInfo()
    }

    override fun getFromMarionnaud(url: String): RawProductInfo {
        //Sephora doesn't like Marionnaud as well
        return RawProductInfo()
    }
}