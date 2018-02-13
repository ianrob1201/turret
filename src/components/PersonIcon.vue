<template>
  <svg width="110" height="110">
    <circle cx="55" cy="55" r="50"/>
    <text x="10" y="75" font-family="monospace" font-size="75">
      {{ initials }}
    </text>
    </svg>
</template>

<script>
	export default {
	  name: 'PersonIcon',
	  props: [
		  'initials'
	  ]
	}
</script>

<style scoped>
 text {
  stroke: red;
  fill: red;
 }

 circle {
  stroke: blue;
  fill: blue;
 }
</style>