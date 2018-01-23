package com.example.ddas.workaholic;


import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;


/**
 * Created by ddas on 24/10/17.
 */

public class SplashActivity extends AppCompatActivity{

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Intent intent = new Intent(this,MainActivity.class);
        startActivity(intent);
        finish();
    }
}
