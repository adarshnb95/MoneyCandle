package com.adarshnb.moneycandle.network

import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface MoneyCandleApiService {

    @GET("alerts")
    suspend fun getAlerts(): List<AlertDto>

    @POST("alerts")
    suspend fun createAlert(
        @Body body: CreateAlertRequest
    ): AlertDto

    @POST("alerts/check")
    suspend fun checkAlerts(
        @Body body: AlertCheckRequest
    ): List<TriggeredAlertDto>
}
