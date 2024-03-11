<script setup>
import { RouterView } from 'vue-router';
import NavigationMenu from '@/NavigationMenu.vue';

</script>
<template>
    <section class="page-layout">

        <section class="side-navigation">
            <aside>
                <NavigationMenu />
            </aside>
        </section>

        <section class="main-content">
            <div>
                <slot name="pageMenu"></slot>
            </div>
            <div>
                <slot name="childComponent">
                    <RouterView />
                </slot>
            </div>

        </section>

    </section>

</template>