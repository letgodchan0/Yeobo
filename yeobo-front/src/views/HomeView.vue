<template>
  <div>
    <div>
      <h2>검색 기능 + 핀 기능 + 넘어온 좌표 보여주는 기능</h2>
      <GmapAutocomplete
        @place_changed='setPlace'
      />
      <button
        @click='addMarker'
      >
        Add
      </button>
      <p id="latLng">위도와 경도</p>
    </div>
    <br>
    <GmapMap
      :center='center'
      :zoom='12'
      style='width: 1000px;  height: 800px; float: right;'
    >
      <GmapMarker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
      />
    </GmapMap>
  </div>
</template>

<script>
var locations = [
  ['명동', 37.563576, 126.983431],
  ['가로수길', 37.520300, 127.023008],
  ['광화문', 37.575268, 126.976896],
  ['남산', 37.550925, 126.990945],
  ['이태원', 37.540223, 126.994005]
];

export default {
  name: 'GoogleMap',
  data() {
    return {
      sample_location: {lat: 37.566, lng: 126.978},
      center: { lat: 45.508, lng: -73.587 },
      currentPlace: null,
      markers: [],
      places: [],
    }
  },
  mounted() {
    this.geolocate();
    for (var i = 0; i < locations.length; i++) {
      this.markers.push({
        position: {
          lat: locations[i][1],
          lng: locations[i][2]
        }
      });
    }
  },

  methods: {
    onClickMarker(marker) {
      this.center=marker.position;
      this.zoom='70';
    },
    setPlace(place) {
      this.currentPlace = place;
    },
    addMarker() {
      if (this.currentPlace) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng(),
        };
        this.markers.push({ position: marker });
        this.places.push(this.currentPlace);
        this.center = marker;
        this.currentPlace = null;
        var el = document.getElementById('latLng');
        el.innerHTML = '위도: ' + marker.lat + ' 경도: ' + marker.lng;
      }
    },
    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
      });
    },
  },
};
</script>