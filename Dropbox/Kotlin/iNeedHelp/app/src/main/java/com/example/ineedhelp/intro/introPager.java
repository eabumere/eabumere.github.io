package com.example.ineedhelp.intro;

import androidx.appcompat.app.AppCompatActivity;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;


import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;

import com.example.ineedhelp.engine.MainActivity;
import com.example.ineedhelp.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class introPager extends AppCompatActivity {
    private FirebaseAuth mAuth;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
//        setTheme(R.style.AppTheme);
        super.onCreate(savedInstanceState);
        mAuth = FirebaseAuth.getInstance();

        setContentView(R.layout.intropage);
        // Initialize Firebase Auth



    }
    public boolean isUserSigned(){
        return false;
    };

    @Override
    public void onStart() {
        super.onStart();
        // Check if user is signed in (non-null) and update UI accordingly.
        FirebaseUser currentUser = mAuth.getCurrentUser();
        checkCurrentUser(currentUser);
    }

    private void checkCurrentUser(FirebaseUser user){

        if(user == null){
            System.out.println("User is not signed");
            FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
            //  Fragment fragment;
            Fragment fragment = new welcome();
            transaction.replace(R.id.flContainer, fragment);
            transaction.commit();

        }else{
            SharedPreferences sharedPref = getSharedPreferences("userlogged", Context.MODE_PRIVATE);
            SharedPreferences.Editor editor = sharedPref.edit();
            editor.putString("userlogged", user.getEmail());
            editor.commit();

            Intent intent = new Intent(introPager.this, MainActivity.class);
            startActivity(intent);
        }

    }
}