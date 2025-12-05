package com.example.moneycandle.network  // change to your actual package

import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

enum class AlertDirection {
    @field:Json(name = "above")
    ABOVE,

    @field:Json(name = "below")
    BELOW
}

@JsonClass(generateAdapter = true)
data class AlertDto(
    val id: Int,
    val symbol: String,
    @field:Json(name = "target_price") val targetPrice: Double,
    val direction: AlertDirection,
    @field:Json(name = "created_at") val createdAt: String
)

@JsonClass(generateAdapter = true)
data class CreateAlertRequest(
    val symbol: String,
    @field:Json(name = "target_price") val targetPrice: Double,
    val direction: AlertDirection
)

@JsonClass(generateAdapter = true)
data class PriceSnapshot(
    val symbol: String,
    val price: Double
)

@JsonClass(generateAdapter = true)
data class AlertCheckRequest(
    val prices: List<PriceSnapshot>
)

@JsonClass(generateAdapter = true)
data class TriggeredAlertDto(
    val alert: AlertDto,
    @field:Json(name = "current_price") val currentPrice: Double
)
