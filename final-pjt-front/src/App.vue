<template>
  <v-app>
    <NavBar v-if="showHeaderAndNav" />
    <router-view @route-change="updateVisibility"></router-view>
    <Footer v-if="showHeaderAndNav" />
  </v-app>
</template>

<script setup>

import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

const showHeaderAndNav = ref(true);
const route = useRoute();

const updateVisibility = () => {
  // 초기 화면 경로를 '/'로 가정합니다.
  const hiddenPaths = ['/', '/login', '/signup'];
  showHeaderAndNav.value = !hiddenPaths.includes(route.path);
};

// 초기 경로에 대한 가시성 설정
updateVisibility();

// 경로가 변경될 때마다 업데이트
watch(route, () => {
  updateVisibility();
});
</script>