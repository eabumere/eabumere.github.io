package com.example.ineedhelp.Database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {


    // Database Version
    private static  int DATABASE_VERSION = 1;

    // Database Name
    private static String DATABASE_NAME = "iNeedHelpMain.db";

    // User table name
    private static String TABLE_USER = "iNeedHelpMain";
    /**
     * Constructor
     *
     * @param context
     */
    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(CREATE_USER_TABLE);

    }
}
