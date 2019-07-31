
qcloudcli scf CreateFunction \\\
--functionName "hello" \\\
--code "@$(zip -r - * |base64)" \\\
--handler "hello.main_handler" \\\
--description "my first scf"