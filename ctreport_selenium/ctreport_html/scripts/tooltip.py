content = '''
    <script>
        $(document).ready(function(){
          $('#testdetails').tooltip().mouseover();
			setTimeout(function(){ $('#testdetails').tooltip('hide'); }, 5000);
			$('[data-toggle="tooltip"]').tooltip();
        });
    </script>
    '''
