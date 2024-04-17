package org.kivy.bootup;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class MyReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        try {
            System.out.println("INSIDE REGISTER RECEIVER");
            String action = intent.getAction();
            if (action != null) {
                if (action.equals(Intent.ACTION_BOOT_COMPLETED) || action.equals(Intent.ACTION_LOCKED_BOOT_COMPLETED)) {
                    System.out.println("TESTER BOOTED SUCCESSFULLY");
                }
            }
        } catch (Exception e) {
            System.out.println("EXCEPTION : " + e.getMessage());
        }
    }
}