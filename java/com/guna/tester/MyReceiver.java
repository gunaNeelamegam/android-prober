package com.guna.tester;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;


public class MyReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        try {
            System.out.println("INSIDE BROADCAST RECEIVER");
            String action = intent.getAction();
            if (action != null) {
                if (action.equals(Intent.ACTION_BOOT_COMPLETED) || action.equals(Intent.ACTION_LOCKED_BOOT_COMPLETED)) {
                    Log.d("MyReceiver", "TESTER BOOTED SUCCESSFULLY");
                }
            }
        } catch (Exception e) {
            Log.e("MyReceiver", "EXCEPTION: " + e.getMessage());
        }
    }
}