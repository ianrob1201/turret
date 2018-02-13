<template>
  <div id="app">
    <div id="header">
      <h1>Auto Turret</h1>
      <div>No one is safe!</div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#header {
  background-color: grey;
  position: absolute;
  top: 0;
  width: 100%;
}

#header h1 {
  display: inline;
  left: 0;
  width: 10;
}

#header div {
  display: inline;
}
</style>
