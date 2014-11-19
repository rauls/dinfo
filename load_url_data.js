      function load_url_data(url) {
      	var xmlDoc = null ;
        if (typeof window.ActiveXObject != 'undefined' ) {
          xmlDoc = new ActiveXObject("Microsoft.XMLHTTP");
        }
        else {
          xmlDoc = new XMLHttpRequest();
        }
        xmlDoc.open( "GET", url, false );
        xmlDoc.send( null );
        return xmlDoc.responseText.substring(4) ;
      }
