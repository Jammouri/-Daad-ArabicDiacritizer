import 'package:flutter/material.dart';

class FirstPage_ar extends StatelessWidget{
  const FirstPage_ar({super.key});
 
  

  @override
  Widget build(context){
    return  Scaffold(
      body: Container(color: Colors.white,
              child: Center(
                  child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                   Center(
          child:Column(mainAxisSize: MainAxisSize.min,
          children: [

             Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                const SizedBox(width :280),
                OutlinedButton(onPressed: (){
                  Navigator.pushNamed(context, '/');
                },style: OutlinedButton.styleFrom(
                   foregroundColor: Colors.white,
              backgroundColor: const Color.fromARGB(255, 22, 82, 24)
                ), child: const Text('english'))
              ],
              ),

            Image.asset(
              'assets/images/app_logo.png',
              width:100,
              color:const Color.fromARGB(255, 22, 82, 24),
            ),
            const SizedBox(height:20),
        
             const Text(" أهلا و سهلا في ض",
            style: TextStyle(
              color:Colors.white,fontSize: 15
            ),
            ),
            const SizedBox(height:20),
            OutlinedButton(onPressed:(){
              Navigator.pushNamed(context,'/dia_ar',arguments: 'hfgh',);
            },
            style:OutlinedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: const Color.fromARGB(255, 22, 82, 24)
            ),
            child:const Text("لنبدأ"))
          ]
          ),
          ),
                    ],),
                  ),
    
      ),
    );
    
  }
   





}