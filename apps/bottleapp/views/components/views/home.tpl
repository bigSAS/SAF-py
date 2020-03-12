<script type="text/x-template" id="home">
  <div>
    <div class="row">
      <div class="col text-center">
        <h1>{$msg$}</h1>
        <h2><strong class="red">SAS</strong> kodzi :)</h2>
      </div>
    </div>
    <div class="row">
      <div class="col text-center">
        <img :src="gifUrl" style="width: 100%;">
      </div>
    </div>
  </div>
</script>

<script>
const Home = {
  delimiters: ['{$', '$}'],
  template: '#home',
  data: function () {
    return {
      msg: 'O co tu chodzi?',
      gifUrl: 'https://66.media.tumblr.com/' +
        'f185966a4f504754a72eed4092d4bd67/' +
        'tumblr_mpygmpPJre1rilo3mo1_500.gif'
    }
  }
}
</script>

