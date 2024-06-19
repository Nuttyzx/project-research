<script setup>
const props = defineProps({
  show: Boolean,
  headbgcolor: String
})
const emit = defineEmits(['close']);
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-container">
        <div :class="['modal-header', headbgcolor]">
          <slot name="header"></slot>
        </div>

        <div class="modal-body">
          <slot name="body"></slot>
        </div>

        <div class="modal-footer">
          <slot name="footer">
          </slot>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}

.modal-container {
  min-width: 300px;
  max-width: 95%;
  margin: auto;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  padding-bottom: 20px;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.headder-blue {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: #5b70ef;
  padding: 20px 30px;
  color: #fff;
}

.modal-body {
  padding: 20px;
  max-height: 700px;
  overflow-y: auto;
}

.modal-footer {
  padding-left: 20px;
  padding-right: 20px;
}

.modal-default-button {

}

.modal-default-left {
  float: left;
}

.modal-default-right {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>