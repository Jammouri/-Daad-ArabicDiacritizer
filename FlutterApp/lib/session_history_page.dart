import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


class SessionHistoryPage extends StatefulWidget {
  @override
  State<SessionHistoryPage> createState() {
    return _SessionHistoryPageState();
  }
}

class _SessionHistoryPageState extends State<SessionHistoryPage> {
  @override
  Widget build(context) {
    List<Widget> sessionHistory = Provider.of<SessionHistory>(context).items;
    return Scaffold(body:
        Container(color:Colors.white,
          child: Center(
            child: Column(mainAxisSize: MainAxisSize.max,
                    children:
                     [
                        Image.asset(
                          'assets/images/app_logo.png',
                          width: 100,
                          color: const Color.fromARGB(255, 22, 82, 24),
                        ),
                      Row(
                        children: [
                          const SizedBox(height:150),
                          OutlinedButton.icon(onPressed: (){Navigator.pop(context);},style: OutlinedButton.styleFrom(
                        backgroundColor: const Color.fromARGB(255, 22, 82, 24)), icon:const Icon(Icons.arrow_back,color:Colors.white), label:const Text(''))
                        ],
                      ),
            
                       Expanded(
                child: ListView.builder(
                  itemCount: sessionHistory.length,
                  itemBuilder: (context, index) {
                    return ListTile(
                      title: sessionHistory[index],
                    );
                  }
                ),

            ),
            
                      ],
                  ),
          ),
        )

    );

  
  }
}

class SessionHistory extends ChangeNotifier {
  final List<Widget> _items = [];

  List<Widget> get items => _items;

  void add(Widget item) {
    _items.add(item);
    notifyListeners();
  }
}
