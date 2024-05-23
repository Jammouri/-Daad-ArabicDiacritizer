import 'package:flutter/material.dart';


class FirstPage extends StatelessWidget{
  const FirstPage({super.key});
 
  

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
                const SizedBox(width :300),
                OutlinedButton(onPressed: (){
                  Navigator.pushNamed(context, '/first_ar');
                },style: OutlinedButton.styleFrom(
                   foregroundColor: Colors.white,
              backgroundColor: const Color.fromARGB(255, 22, 82, 24)
                ), child: const Text('عربي'))
              ],

              
            ),
            Image.asset(
              'assets/images/app_logo.png',
              width:100,
              color:const Color.fromARGB(255, 22, 82, 24),
            ),
            const SizedBox(height:20),
        
             const Text("welcome to ض",
            style: TextStyle(
              color:Colors.white,fontSize: 15
            ),
            ),
            const SizedBox(height:20),
            OutlinedButton(onPressed:(){
              Navigator.pushNamed(context,'/dia',arguments: 'hfgh',);
            },
            style:OutlinedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: const Color.fromARGB(255, 22, 82, 24)
            ),
            child:const Text("lets get started"))
          ]
          ),
          ),
                    ],),
                  ),
    
      ),
    );
    
  }
   





}