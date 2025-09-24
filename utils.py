import logging
from django.core.exceptions import ObjectDoesNotExist
from .models import Order

logger = logging.getLogger(__name__)

def update_order_status(order_id, new_status):

    try:
        order = Order.objects.get(id=order_id)
        old_status = order.new_status
        order.status = new_status
        order.save()

        logger.info(
            f"Order {order_id} status updated from '{old_status}' to '{new_status}'."
        )

        return order

    except ObjectDoesNotExist:
        logger.error(f"Order with ID {order_id} not found.")

    except Exception as e:
        logger.error(f"Error updating order {order_id} status: {str(e)}")
        return None