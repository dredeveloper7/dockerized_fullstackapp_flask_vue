<template>
  <div>
    <!-- Your component's content here -->
    {{responseData}}
  </div>
</template>

<script>
export default {
  data() {
    return {
      responseData: null, // Store the response data here
    };
  },
  created() {
    this.fetchData(); // Call the fetchData method when the component is created
  },
  methods: {
    fetchData() {
      fetch('/backend/')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json(); // or response.text() if expecting plain text
        })
        .then(data => {
          // Handle the response data
          this.responseData = data;
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
    },
  },
};
</script>
