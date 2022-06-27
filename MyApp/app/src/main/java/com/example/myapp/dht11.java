package com.example.myapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class dht11 extends AppCompatActivity {
    ListView myListView;
    ArrayList<String> list;
    ArrayAdapter<String> Adapter;
    FirebaseDatabase databaseRef;
    DatabaseReference ref;
    Button Logout,check;
    Data data;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dht11);
        Logout= findViewById(R.id.button);
        check= findViewById(R.id.button2);

        data = new Data();
        databaseRef= FirebaseDatabase.getInstance();
        ref=databaseRef.getReference("dht11");
        list =new ArrayList<String>();
        Adapter = new ArrayAdapter<String>(this,R.layout.data_info,R.id.datainfo ,list);

        myListView = (ListView) findViewById(R.id.listview);

        ref.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                for(DataSnapshot ds:snapshot.getChildren()){
                    data=ds.getValue(Data.class);
                    list.add(data.getTime()+ "  Humidity: "+data.getHumidity()+"%" +"  Temperature: "+data.getTemperature()+ "°C");

                }
                myListView.setAdapter(Adapter);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });




    }
    public void Logout (View view) {
        FirebaseAuth.getInstance().signOut();
        startActivity(new Intent(getApplicationContext(),Login.class));
        finish();
    }
    public void check (View view) {
        FirebaseAuth.getInstance().signOut();
        startActivity(new Intent(getApplicationContext(),CheckActivity.class));
        finish();
    }
}