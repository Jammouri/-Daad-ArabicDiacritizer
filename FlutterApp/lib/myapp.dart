import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:test/first_page.dart';
import 'package:test/diactarizarion_screen.dart';
import 'package:test/first_page_ar.dart';
import 'package:test/generated/l10n.dart';
import 'package:test/session_history_page.dart';
import 'package:test/diacatarization_screen_ar.dart';
import 'package:provider/provider.dart';



class myApp extends StatefulWidget {
  @override
  State<myApp> createState(){
    return  _myAppState();
  }
}


class _myAppState extends State<myApp>{
 
  @override
  
  Widget build(context){
   //Widget screenWidget = FirstPage();

return ChangeNotifierProvider( create: (context)=> SessionHistory(),
  child: MaterialApp(
            home: const FirstPage(),
            localizationsDelegates: const [
                  S.delegate,
                  GlobalMaterialLocalizations.delegate,
                  GlobalWidgetsLocalizations.delegate,
                  GlobalCupertinoLocalizations.delegate,
              ],
              supportedLocales: S.delegate.supportedLocales,
              locale: const Locale('ar'),
                initialRoute: '/',
                routes: {
                  '/first_ar':(context)=>const FirstPage_ar(),
                  '/dia':(context)=> const DiactarizationScreen(),
                  '/dia_ar':(context)=>const DiactarizationScreen_ar(),
                  '/his':(context)=> SessionHistoryPage(),
                },
                ),
);

  }



}