package com.adarshnb.moneycandle

import android.os.Bundle
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.moneycandle.ui.theme.MoneyCandleTheme

import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.adarshnb.moneycandle.network.ApiClient
import com.adarshnb.moneycandle.R

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        lifecycleScope.launch {
            try {
                val alerts = ApiClient.api.getAlerts()
                Log.d("API_TEST", "Fetched alerts: $alerts")
            } catch (e: Exception) {
                Log.e("API_TEST", "Error fetching alerts", e)
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    MoneyCandleTheme {
        Greeting("Android")
    }
}