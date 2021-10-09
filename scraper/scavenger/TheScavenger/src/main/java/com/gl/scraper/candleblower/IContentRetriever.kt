package com.gl.scraper.candleblower

import com.gl.scraper.dto.RawProductInfo

interface IContentRetriever {
    fun getContent(url: String) : RawProductInfo
}