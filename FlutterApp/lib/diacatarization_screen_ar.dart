import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:test/session_history_page.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

class DiactarizationScreen_ar extends StatefulWidget {
  const DiactarizationScreen_ar({super.key});

  @override
  State<DiactarizationScreen_ar> createState() {
    return _DiactarizationScreen_arState();
  }
}

class _DiactarizationScreen_arState extends State<DiactarizationScreen_ar> {
  final TextEditingController firstController = TextEditingController();
  final TextEditingController secondController = TextEditingController();
  var temp=TextEditingController();
  DateTime now = DateTime.now();
  final dateFormatter = DateFormat('yyyy-MM-dd');
  final timeFormatter = DateFormat('HH:mm:ss');

  @override
  Widget build(context) {
    //final String title = ModalRoute.of(context)?.settings.arguments as String;

    return Scaffold(
        body: Container(
      color: Colors.white,
      child: Center(
        child: Column(mainAxisSize: MainAxisSize.max, children: [
          Image.asset(
            'assets/images/app_logo.png',
            width: 100,
            color: const Color.fromARGB(255, 22, 82, 24),
          ),
          Row(mainAxisAlignment: MainAxisAlignment.start, children: [
            OutlinedButton.icon(
                onPressed: () {
                  Navigator.pushNamed(context, '/first_ar');
                },
                style: OutlinedButton.styleFrom(
                    backgroundColor: const Color.fromARGB(255, 22, 82, 24)),
                icon: const Icon(Icons.arrow_back, color: Colors.white),
                label: const Text(''))
          ]),
          Row(mainAxisAlignment: MainAxisAlignment.start, children: [
            // OutlinedButton.icon(onPressed: (){ Navigator.of(context).pop();},icon: const Icon(Icons.arrow_back),label: const Text('back'),
            // ),

            OutlinedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/his');
                },
                style: OutlinedButton.styleFrom(
                    foregroundColor: Colors.white,
                    backgroundColor: const Color.fromARGB(255, 22, 82, 24)),
                //history button
                child: const Text("تاريخ")),

            const SizedBox(width: 200),
            OutlinedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/dia');
                },
                style: OutlinedButton.styleFrom(
                    foregroundColor: Colors.white,
                    backgroundColor: const Color.fromARGB(255, 22, 82, 24)),
                child: const Text('english'))
          ]),
          ///////////////////////////////////////////////////////////////////////////////////////////////
          //input the text TEXT
          const Text("أدخل النص",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: Color.fromARGB(255, 22, 82, 24),
                fontSize: 15,
              )),

          ///////////////////////////////////////////////////////////////////////////////////////////
          //first text field
          TextFormField(
            controller: firstController,
            textAlign: TextAlign.right,
            maxLength: 400,
            maxLines: 4,
            keyboardType: TextInputType.text,
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              counterText: "الأكثر 400 حرف",
              counterStyle: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 22, 82, 24)),
            ),
            style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: Color.fromARGB(255, 22, 82, 24)),
          ),

          OutlinedButton(
            onPressed: () {
              http.post(
                      Uri.parse(
                          'https://5720-2a01-9700-14e2-b700-90fd-44f6-3e7e-759.ngrok-free.app'),
                      headers: <String, String>{
                        'Content-Type': 'application/json; charset=UTF-8',
                      },
                      body: jsonEncode(
                          <String, String>{'text': firstController.text}))
                  .then((response) {
                // Parse the response body as JSON
                Map<String, dynamic> responseData =
                    json.decode(utf8.decode(response.bodyBytes));

                // Process the API response
                if (response.statusCode == 200) {
                  // API request was successful
                  secondController.text = responseData['diacatarize'];
                } else {
                  // API request failed
                  secondController.text = response.reasonPhrase!;
                }
              }).catchError((error) {
                // Handle any errors that occurred during the request
                print('Request error: $error');
              });

               if (firstController.text.isNotEmpty) {
                  Provider.of<SessionHistory>(context, listen: false).add(
                    Column(children: [
                      Text(timeFormatter.format(now)),
                      const SizedBox(
                        height: 10,
                      ),
                      Text(dateFormatter.format(now)),
                      const SizedBox(
                        height: 10,
                      ),
                      Text(firstController.text),
                    ]),
                  );
                }
              },
            style: OutlinedButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: const Color.fromARGB(255, 22, 82, 24)),
            child: const Text("شكل"),
          ),

          const SizedBox(height: 10),
          //////////////////////////////////////////////////////////////////////////////////////////////////////
          //output text
          const Text("النتيجة",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: Color.fromARGB(255, 22, 82, 24),
                fontSize: 15,
              )),

          /////////////////////////////////////////////////////////////////////////////////////
          //second text field
          TextFormField(
            controller: secondController,
            textAlign: TextAlign.right,
            readOnly: true,
            maxLength: 400,
            maxLines: 4,
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              counterText: "الأكثر 400 حرف",
              counterStyle: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 22, 82, 24)),
            ),
            style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: Color.fromARGB(255, 22, 82, 24)),
          ),
        ]),
      ),
    ));
  }
}
