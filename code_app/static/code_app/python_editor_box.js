        function update()
    {
        var idoc = document.getElementById('iframe').contentWindow.document;
        var form = document.getElementById("answer");

        idoc.open();
        idoc.write(editor.getValue());
        idoc.close();
        form.value=editor.getValue();
    }

    function setupEditor()
    {
      window.editor = ace.edit("editor");
      editor.setTheme("ace/theme/monokai");
      editor.getSession().setMode("ace/mode/python");
      editor.setValue(``,1); //1 = moves cursor to end (możemy tu dować wartość defoultową która ma się wyświetlać w boxie kodu)

      editor.getSession().on('change', function() {
        update();
      });

      editor.focus();


      editor.setOptions({
        fontSize: "16pt",
        showLineNumbers: false,
        showGutter: false,
        vScrollBarAlwaysVisible:true,
        enableBasicAutocompletion: false, enableLiveAutocompletion: false
      });

      editor.setShowPrintMargin(false);
      editor.setBehavioursEnabled(false);
    }

    setupEditor();
    update();